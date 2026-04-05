from __future__ import annotations

import json
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox

from classes import Factory, topNforUpgrade, bestConfig
from factories import FACTORY_CONTRACTS
from res import RESOURCES
from pathlib import Path
import tempfile

CONFIG_PATH = Path(tempfile.gettempdir()) / 'resources-tool-config.json'

# config_key, contract_key
FACTORY_SPECS = [
    ("bricks", "brick"),
    ("concrete", "concrete"),
    ("fertilizer", "fertilizer"),
    ("steel", "steel"),
    ("fuel", "fuel"),
    ("glass", "glass"),
    ("copper", "copper"),
    ("insecticide", "insecticide"),
    ("aluminum", "aluminum"),
    ("plastic", "plastic"),
    ("lithium", "lithium"),
    ("accumulator", "accumulator"),
    ("weapons", "weapons"),
    ("silicon", "silicon"),
    ("circuitry", "circuitry"),
    ("titanium", "titanium"),
    ("medtech", "medtech"),
    ("silver", "silver"),
    ("gold", "gold"),
    ("jewellery", "jewellery"),
    ("drone", "drone"),
    ("trucks", "trucks"),
]

FACTORY_LABELS = {
    "bricks": "Кирпичный завод",
    "concrete": "Бетонный завод",
    "fertilizer": "Завод удобрений",
    "steel": "Сталелитейный завод",
    "fuel": "Топливный завод",
    "glass": "Стекольный завод",
    "copper": "Медеплавильный завод",
    "insecticide": "Завод инсектицидов",
    "aluminum": "Алюминиевый завод",
    "plastic": "Завод пластика",
    "lithium": "Литиевый завод",
    "accumulator": "Аккумуляторный завод",
    "weapons": "Оружейный завод",
    "silicon": "Кремниевый завод",
    "circuitry": "Электронный завод",
    "titanium": "Титановый завод",
    "medtech": "Завод медтехники",
    "silver": "Сереброплавильный завод",
    "gold": "Золотодобывающий завод",
    "jewellery": "Ювелирный завод",
    "drone": "Завод дронов",
    "trucks": "Автозавод",
}

RESOURCE_LABELS = {
    "money": "Деньги",
    "concrete": "Бетон",
    "bricks": "Кирпич",
    "steel": "Сталь",
    "fuel": "Топливо",
    "copper": "Медь",
    "glass": "Стекло",
    "aluminum": "Алюминий",
    "plastic": "Пластик",
    "medtech": "Медтехника",
    "titanium": "Титан",
    "circuitry": "Электроника",
    "insecticide": "Инсектицид",
    "lithium": "Литий",
    "accumulator": "Аккумулятор",
    "weapons": "Оружие",
    "silicon": "Кремний",
    "silver": "Серебро",
    "gold": "Золото",
    "fertilizer": "Удобрение",
    "trucks": "Грузовики",
    "drone": "Дрон",
    "jewellery": "Ювелирные изделия",
    "clay": "Глина",
    "limestone": "Известняк",
    "gravel": "Гравий",
    "iron": "Железо",
    "coal": "Уголь",
    "crude_oil": "Сырая нефть",
    "copper_ore": "Медная руда",
    "bauxite": "Бокситы",
    "sand": "Песок",
    "lithium_ore": "Литиевая руда",
    "ilmenite": "Ильменит",
    "silver_ore": "Серебряная руда",
    "gold_ore": "Золотая руда",
    "diamond": "Алмаз",
}

RESOURCE_MAP = {resource.name: resource for resource in RESOURCES}


def factory_label(name: str) -> str:
    return FACTORY_LABELS.get(name, name)


def resource_label(name: str) -> str:
    return RESOURCE_LABELS.get(name, name)


class AppState:
    def __init__(self) -> None:
        self.factory_rows = {
            config_key: {"contract_key": contract_key, "lvl": 0, "speed_mult": 1.0}
            for config_key, contract_key in FACTORY_SPECS
        }
        self.resource_rows = {resource.name: float(resource.price) for resource in RESOURCES}

    def to_config(self) -> dict:
        return {
            "factories": {
                name: {
                    "lvl": row["lvl"],
                    "speed_mult": row["speed_mult"],
                }
                for name, row in self.factory_rows.items()
            },
            "resources": dict(self.resource_rows),
        }

    @classmethod
    def from_config(cls, config: dict) -> "AppState":
        state = cls()

        factory_config = config.get("factories", {})
        for config_key, row in state.factory_rows.items():
            data = factory_config.get(config_key)
            if data is None and config_key == "bricks":
                data = factory_config.get("brick")
            if not data:
                continue
            row["lvl"] = int(data.get("lvl", row["lvl"]))
            row["speed_mult"] = float(data.get("speed_mult", row["speed_mult"]))

        resource_config = config.get("resources", {})
        for resource_name in state.resource_rows:
            if resource_name in resource_config:
                state.resource_rows[resource_name] = float(resource_config[resource_name])

        return state

    def apply_prices_to_resources(self) -> None:
        for resource_name, price in self.resource_rows.items():
            RESOURCE_MAP[resource_name].price = float(price)

    def build_factories(self) -> list[Factory]:
        self.apply_prices_to_resources()
        factories: list[Factory] = []
        for config_key, row in self.factory_rows.items():
            factories.append(
                Factory(
                    factory_label(config_key),
                    FACTORY_CONTRACTS[row["contract_key"]],
                    int(row["lvl"]),
                    float(row["speed_mult"]),
                )
            )
        return factories


def build_default_config() -> dict:
    return AppState().to_config()


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        config = build_default_config()
        save_config(config)
        return config

    try:
        return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        config = build_default_config()
        save_config(config)
        return config


def save_config(config: dict) -> None:
    CONFIG_PATH.write_text(
        json.dumps(config, indent=4, ensure_ascii=False),
        encoding="utf-8",
    )


class ResourcesToolApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Resources Tool")
        self.geometry("1180x760")
        self.minsize(980, 640)

        self.state_model = AppState.from_config(load_config())

        self._build_style()
        self._build_ui()
        self.refresh_all_views()

    def _build_style(self) -> None:
        style = ttk.Style(self)
        try:
            style.theme_use("vista")
        except tk.TclError:
            pass
        style.configure("Header.TLabel", font=("Segoe UI", 15, "bold"))
        style.configure("SubHeader.TLabel", font=("Segoe UI", 10, "bold"))

    def _build_ui(self) -> None:
        container = ttk.Frame(self, padding=12)
        container.pack(fill="both", expand=True)

        header = ttk.Frame(container)
        header.pack(fill="x", pady=(0, 10))

        ttk.Label(header, text="Resources Tool", style="Header.TLabel").pack(side="left")

        actions = ttk.Frame(header)
        actions.pack(side="right")

        ttk.Button(actions, text="Загрузить конфиг", command=self.on_reload).pack(side="left", padx=4)
        ttk.Button(actions, text="Сохранить конфиг", command=self.on_save).pack(side="left", padx=4)
        ttk.Button(actions, text="Сбросить по умолчанию", command=self.on_reset).pack(side="left", padx=4)

        self.notebook = ttk.Notebook(container)
        self.notebook.pack(fill="both", expand=True)

        self.tab_calc = ttk.Frame(self.notebook, padding=10)
        self.tab_factories = ttk.Frame(self.notebook, padding=10)
        self.tab_resources = ttk.Frame(self.notebook, padding=10)
        self.tan_authors = ttk.Frame(self.notebook, padding=10)

        self.notebook.add(self.tab_calc, text="Расчёты")
        self.notebook.add(self.tab_factories, text="Заводы")
        self.notebook.add(self.tab_resources, text="Ресурсы")
        self.notebook.add(self.tan_authors, text="Авторы")

        self._build_calc_tab()
        self._build_factories_tab()
        self._build_resources_tab()
        self._build_authors_tab()

    def _build_calc_tab(self) -> None:
        top = ttk.Frame(self.tab_calc)
        top.pack(fill="x", pady=(0, 10))

        ttk.Label(top, text="Режим расчёта", style="SubHeader.TLabel").grid(row=0, column=0, sticky="w")

        self.calc_mode = tk.StringVar(value="top")
        self.calc_count = tk.StringVar(value="10")

        mode_frame = ttk.Frame(top)
        mode_frame.grid(row=1, column=0, sticky="w", pady=(4, 0))

        ttk.Radiobutton(mode_frame, text="Топ N апов с текущего уровня", variable=self.calc_mode, value="top").pack(side="left", padx=(0, 12))
        ttk.Radiobutton(mode_frame, text="Лучшая конфигурация с нуля", variable=self.calc_mode, value="best").pack(side="left")

        count_frame = ttk.Frame(top)
        count_frame.grid(row=2, column=0, sticky="w", pady=(10, 0))

        ttk.Label(count_frame, text="Количество:").pack(side="left")
        ttk.Entry(count_frame, width=10, textvariable=self.calc_count).pack(side="left", padx=6)
        ttk.Button(count_frame, text="Рассчитать", command=self.on_calculate).pack(side="left", padx=6)

        hint = ttk.Label(
            top,
            text="Текущие значения берутся из вкладок «Заводы» и «Ресурсы».",
        )
        hint.grid(row=3, column=0, sticky="w", pady=(10, 0))

        result_frame = ttk.Frame(self.tab_calc)
        result_frame.pack(fill="both", expand=True)

        self.result_text = tk.Text(result_frame, wrap="word", font=("Consolas", 11))
        self.result_text.pack(side="left", fill="both", expand=True)

        result_scroll = ttk.Scrollbar(result_frame, orient="vertical", command=self.result_text.yview)
        result_scroll.pack(side="right", fill="y")
        self.result_text.configure(yscrollcommand=result_scroll.set)

    def _build_factories_tab(self) -> None:
        ttk.Label(self.tab_factories, text="Настройка заводов", style="SubHeader.TLabel").pack(anchor="w", pady=(0, 8))

        frame = ttk.Frame(self.tab_factories)
        frame.pack(fill="both", expand=True)

        columns = ("name", "lvl", "speed_mult")
        self.factories_tree = ttk.Treeview(frame, columns=columns, show="headings", height=18)
        self.factories_tree.heading("name", text="Завод")
        self.factories_tree.heading("lvl", text="Уровень")
        self.factories_tree.heading("speed_mult", text="Множитель скорости")
        self.factories_tree.column("name", width=220)
        self.factories_tree.column("lvl", width=120, anchor="center")
        self.factories_tree.column("speed_mult", width=160, anchor="center")
        self.factories_tree.pack(side="left", fill="both", expand=True)
        self.factories_tree.bind("<<TreeviewSelect>>", self.on_factory_select)

        scroll = ttk.Scrollbar(frame, orient="vertical", command=self.factories_tree.yview)
        scroll.pack(side="right", fill="y")
        self.factories_tree.configure(yscrollcommand=scroll.set)

        editor = ttk.LabelFrame(self.tab_factories, text="Редактор", padding=10)
        editor.pack(fill="x", pady=(10, 0))

        self.factory_name_var = tk.StringVar()
        self.factory_lvl_var = tk.StringVar()
        self.factory_speed_var = tk.StringVar()

        ttk.Label(editor, text="Завод:").grid(row=0, column=0, sticky="w")
        ttk.Entry(editor, textvariable=self.factory_name_var, state="readonly", width=24).grid(row=0, column=1, sticky="w", padx=(6, 18))

        ttk.Label(editor, text="Уровень:").grid(row=0, column=2, sticky="w")
        ttk.Entry(editor, textvariable=self.factory_lvl_var, width=12).grid(row=0, column=3, sticky="w", padx=(6, 18))

        ttk.Label(editor, text="Скорость:").grid(row=0, column=4, sticky="w")
        ttk.Entry(editor, textvariable=self.factory_speed_var, width=12).grid(row=0, column=5, sticky="w", padx=(6, 18))

        ttk.Button(editor, text="Применить", command=self.on_factory_apply).grid(row=0, column=6, padx=6)
        ttk.Button(editor, text="Сбросить выделенный", command=self.on_factory_reset_selected).grid(row=0, column=7, padx=6)

    def _build_authors_tab(self) -> None:
        ttk.Label(self.tan_authors, text="calculations - FinalTry\nGUI - egoryanasy", style="SubHeader.TLabel").pack(anchor="w", pady=(0, 10))

    def _build_resources_tab(self) -> None:
        ttk.Label(self.tab_resources, text="Настройка цен ресурсов", style="SubHeader.TLabel").pack(anchor="w", pady=(0, 8))

        frame = ttk.Frame(self.tab_resources)
        frame.pack(fill="both", expand=True)

        left = ttk.Frame(frame)
        left.pack(side="left", fill="both", expand=True)

        search_bar = ttk.Frame(left)
        search_bar.pack(fill="x", pady=(0, 8))

        ttk.Label(search_bar, text="Поиск:").pack(side="left")
        self.resource_search_var = tk.StringVar()
        self.resource_search_var.trace_add("write", lambda *_: self.refresh_resources_tree())
        ttk.Entry(search_bar, textvariable=self.resource_search_var).pack(side="left", padx=6, fill="x", expand=True)

        columns = ("name", "price")
        self.resources_tree = ttk.Treeview(left, columns=columns, show="headings", height=20)
        self.resources_tree.heading("name", text="Ресурс")
        self.resources_tree.heading("price", text="Цена")
        self.resources_tree.column("name", width=260)
        self.resources_tree.column("price", width=160, anchor="e")
        self.resources_tree.pack(side="left", fill="both", expand=True)
        self.resources_tree.bind("<<TreeviewSelect>>", self.on_resource_select)

        scroll = ttk.Scrollbar(left, orient="vertical", command=self.resources_tree.yview)
        scroll.pack(side="right", fill="y")
        self.resources_tree.configure(yscrollcommand=scroll.set)

        editor = ttk.LabelFrame(frame, text="Редактор", padding=10)
        editor.pack(side="right", fill="y", padx=(10, 0))

        self.resource_name_var = tk.StringVar()
        self.resource_price_var = tk.StringVar()

        ttk.Label(editor, text="Ресурс:").grid(row=0, column=0, sticky="w")
        ttk.Entry(editor, textvariable=self.resource_name_var, state="readonly", width=22).grid(row=1, column=0, sticky="w", pady=(4, 10))

        ttk.Label(editor, text="Цена:").grid(row=2, column=0, sticky="w")
        ttk.Entry(editor, textvariable=self.resource_price_var, width=22).grid(row=3, column=0, sticky="w", pady=(4, 10))

        ttk.Button(editor, text="Применить", command=self.on_resource_apply).grid(row=4, column=0, sticky="ew", pady=4)
        ttk.Button(editor, text="Сбросить выделенный", command=self.on_resource_reset_selected).grid(row=5, column=0, sticky="ew", pady=4)

    def refresh_all_views(self) -> None:
        self.refresh_factories_tree()
        self.refresh_resources_tree()
        self.result_text.delete("1.0", tk.END)

    def refresh_factories_tree(self) -> None:
        self.factories_tree.delete(*self.factories_tree.get_children())
        for name, row in self.state_model.factory_rows.items():
            self.factories_tree.insert(
                "",
                tk.END,
                iid=name,
                values=(factory_label(name), row["lvl"], row["speed_mult"]),
            )

    def refresh_resources_tree(self) -> None:
        self.resources_tree.delete(*self.resources_tree.get_children())
        term = self.resource_search_var.get().strip().lower()
        for name, price in sorted(self.state_model.resource_rows.items()):
            label = resource_label(name)
            if term and term not in label.lower() and term not in name.lower():
                continue
            self.resources_tree.insert("", tk.END, iid=name, values=(label, price))

    def on_factory_select(self, _event=None) -> None:
        selection = self.factories_tree.selection()
        if not selection:
            return
        name = selection[0]
        row = self.state_model.factory_rows[name]
        self.factory_name_var.set(factory_label(name))
        self.factory_lvl_var.set(str(row["lvl"]))
        self.factory_speed_var.set(str(row["speed_mult"]))

    def on_resource_select(self, _event=None) -> None:
        selection = self.resources_tree.selection()
        if not selection:
            return
        name = selection[0]
        self.resource_name_var.set(resource_label(name))
        self.resource_price_var.set(str(self.state_model.resource_rows[name]))

    def on_factory_apply(self) -> None:
        selection = self.factories_tree.selection()
        if not selection:
            messagebox.showwarning("Нет выбора", "Сначала выбери завод в таблице.")
            return
        name = selection[0]
        if not name:
            messagebox.showwarning("Нет выбора", "Сначала выбери завод в таблице.")
            return
        try:
            lvl = int(self.factory_lvl_var.get())
            speed = float(self.factory_speed_var.get())
            if lvl < 0:
                raise ValueError
            if speed <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Ошибка", "Уровень должен быть >= 0, а скорость > 0.")
            return

        self.state_model.factory_rows[name]["lvl"] = lvl
        self.state_model.factory_rows[name]["speed_mult"] = speed
        self.refresh_factories_tree()
        self.factories_tree.selection_set(name)
        self.factories_tree.focus(name)

    def on_resource_apply(self) -> None:
        selection = self.resources_tree.selection()
        if not selection:
            messagebox.showwarning("Нет выбора", "Сначала выбери ресурс в таблице.")
            return
        name = selection[0]
        if not name:
            messagebox.showwarning("Нет выбора", "Сначала выбери ресурс в таблице.")
            return
        try:
            price = float(self.resource_price_var.get())
            if price < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Ошибка", "Цена должна быть числом >= 0.")
            return

        self.state_model.resource_rows[name] = price
        self.refresh_resources_tree()
        if self.resources_tree.exists(name):
            self.resources_tree.selection_set(name)
            self.resources_tree.focus(name)

    def on_factory_reset_selected(self) -> None:
        selection = self.factories_tree.selection()
        if not selection:
            return
        name = selection[0]
        self.state_model.factory_rows[name]["lvl"] = 0
        self.state_model.factory_rows[name]["speed_mult"] = 1.0
        self.factory_lvl_var.set("0")
        self.factory_speed_var.set("1.0")
        self.refresh_factories_tree()
        self.factories_tree.selection_set(name)
        self.factories_tree.focus(name)

    def on_resource_reset_selected(self) -> None:
        selection = self.resources_tree.selection()
        if not selection:
            return
        name = selection[0]
        default_price = next(resource.price for resource in RESOURCES if resource.name == name)
        # Возвращаем цену из базового набора ресурсов, а не из текущего состояния.
        original_config = build_default_config()
        self.state_model.resource_rows[name] = float(original_config["resources"][name])
        self.resource_price_var.set(str(self.state_model.resource_rows[name]))
        self.refresh_resources_tree()
        if self.resources_tree.exists(name):
            self.resources_tree.selection_set(name)
            self.resources_tree.focus(name)

    def on_calculate(self) -> None:
        try:
            count = int(self.calc_count.get())
            if count <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Ошибка", "Количество должно быть целым числом > 0.")
            return

        factories = self.state_model.build_factories()

        if self.calc_mode.get() == "top":
            result = topNforUpgrade(factories, count)
        else:
            result = bestConfig(factories, count)

        self.result_text.delete("1.0", tk.END)
        self.result_text.insert("1.0", "\n".join(result))

    def on_save(self) -> None:
        save_config(self.state_model.to_config())
        messagebox.showinfo("Сохранено", "Конфиг успешно сохранён.")

    def on_reload(self) -> None:
        self.state_model = AppState.from_config(load_config())
        self.factory_name_var.set("")
        self.factory_lvl_var.set("")
        self.factory_speed_var.set("")
        self.resource_name_var.set("")
        self.resource_price_var.set("")
        self.refresh_all_views()
        messagebox.showinfo("Готово", "Конфиг заново загружен из файла.")

    def on_reset(self) -> None:
        if not messagebox.askyesno("Подтверждение", "Сбросить настройки к значениям по умолчанию?"):
            return
        self.state_model = AppState.from_config(build_default_config())
        self.factory_name_var.set("")
        self.factory_lvl_var.set("")
        self.factory_speed_var.set("")
        self.resource_name_var.set("")
        self.resource_price_var.set("")
        self.refresh_all_views()


if __name__ == "__main__":
    app = ResourcesToolApp()
    app.mainloop()
