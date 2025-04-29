import os

BASE_DIR = "./"

# Иерархическая структура Vault'а
vault_structure = {
    "00_web": {},
    "01_frontend": {
        "foundations": {
            "html": {},
            "css": {},
            "javascript": {},
            "accessibility": {}
        },
        "frameworks": {
            "react": {},
            "nextjs": {},
            "astro": {},
            "vite": {},
            "wordpress": {}
        },
        "ui-ux": {
            "design": {},
            "layout": {},
            "animations": {},
            "ui-patterns": {},
            "tailwind": {},
            "dark-mode": {}
        },
        "ui-libraries": {
            "shadcn-ui": {},
            "radix-ui": {},
            "geist-ui": {},
            "mantine": {},
            "chakra-ui": {},
            "daisyui": {},
            "headless-ui": {},
            "lucide-icons": {},
            "heroicons": {}
        },
        "state-management": {
            "context-api": {},
            "zustand": {},
            "jotai": {},
            "redux": {},
            "recoil": {},
            "react-query": {}
        }
    },
    "02_backend": {
        "databases": {
            "mongodb": {},
            "prisma": {},
            "postgresql": {},
            "redis": {}
        }
    },
    "03_devtools": {},
    "04_methodologies": {},
    "05_concepts": {},
    "06_deployment": {},
    "07_seo-performance": {},
    "08_notes-discoveries": {},
    "99_meta": {
        "inbox": {},
        "source": {
            "img": {},
            "pdf": {},
            "video": {}
        },
        "templates": {},
        "glossary": {},
        "snippets": {},
        "archive": {},
        "meta": {}
    }
}

def create_structure(base_path, structure):
    for name, children in structure.items():
        path = os.path.join(base_path, name)
        os.makedirs(path, exist_ok=True)

        # Создаём index.md в каждой папке
        index_path = os.path.join(path, "index.md")
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(f"# {name.capitalize()}\n")

        # Рекурсивно проходимся по дочерним структурам
        if isinstance(children, dict):
            create_structure(path, children)

if __name__ == "__main__":
    print("🚀 Создание Obsidian Vault структуры...")
    create_structure(BASE_DIR, vault_structure)
    print(f"✅ Vault создан в: {BASE_DIR}/")
