# Пример расширенной структуры
"""
📁 Obsidian Vault Generator
────────────────────────────
Этот скрипт автоматически создаёт структуру папок и файлов для Obsidian Vault 
на основе заранее заданного словаря `vault_structure`.

🔧 Возможности:
- Создаёт вложенные папки (рекурсивно)
- В каждой папке создаёт `index.md`, если он отсутствует
- Вставляет YAML-заголовок и шаблон контента в `index.md`
- В секции 🔗 Related Notes автоматически добавляет:
    • ссылки на подпапки (через их `index.md`)
    • ссылки на соседние `.md` файлы, указанные в `"__files"`
- Не перезаписывает существующие файлы
- Работает на любой глубине вложенности

📌 Пример структуры:
vault_structure = {
    "01_frontend": {
        "frameworks": {
            "react": {
                "__files": ["hooks.md", "state.md"]
            }
        }
    }
}

🛠 Как использовать:
1. Укажи нужную структуру в переменной `vault_structure`
2. Запусти скрипт: python create_vault.py
3. Скрипт создаст/дополнит директории и шаблоны файлов

🧠 Идеально подходит для систематизации знаний в Obsidian с полной автоматизацией рутины.
"""



vault_structure = {
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
            "components": {
                "buttons": {},
                "cards": {},
                "modals": {},
                "dropdowns": {},
                "tooltips": {},
                "tables": {},
                "charts": {},
                "forms": {
                    "__files": ["input.md", "validation.md", "controlled-vs-uncontrolled.md"]
                }
            },
            "layout": {
            },
            "animations": {
                "framer-motion": {
                    "__files": ["motion.md", "layout.md", "scroll.md", "examples.md"]
                },
                "gsap": {},
                "__files": ["css-animations.md", "best-practices.md"]
            },
            "ui-patterns": {
                "__files": ["cards.md", "dashboards.md", "inputs.md", "modern-minimal-ui.md"],
                "modern-minimal-ui": {}
                
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
            "ui-kits": {
                "tailwind-ui": {
                    "__files": ["overview.md", "components.md"]
                },
                "flowbite": {},
                "daisyui": {},
                "material-ui": {},
                "ant-design": {},
                "bootstrap": {},
                "bulma": {},
                "semantic-ui": {}
            },
            "ui-sources": {
                "icons": {
                    "__files": ["svg.md", "font-icons.md", "icon-fonts.md"],
                    "heroicons": {},
                    "lucide-icons": {},
                    "font-awesome": {},
                    "material-icons": {},
                    "feather-icons": {}
                },
                "fonts": {
                    "__files": ["google-fonts.md", "font-face.md", "font-display.md"],
                    "google-fonts": {},
                    "fontsource": {},
                    "typekit": {},
                    "local-fonts": {}
                },
                "images": {
                    "__files": ["svg.md", "webp.md", "avif.md", "jpeg.md", "png.md"],
                    "unsplash": {},
                    "pexels": {},
                    "shutterstock": {},
                    "freepik": {},
                    "icons8": {}
                },
                "videos": {
                    "__files": ["mp4.md", "webm.md", "ogg.md"],
                    "pexels": {},
                    "unsplash": {},
                    "shutterstock": {},
                    "freepik": {},
                    "icons8": {}
                },
                "audio": {
                    "__files": ["mp3.md", "wav.md", "ogg.md"],
                    "soundcloud": {},
                    "spotify": {},
                    "freepik": {},
                    "icons8": {}
                },
                "patterns": {
                    "__files": ["css-patterns.md", "svg-patterns.md", "backgrounds.md"],
                    "css-patterns": {},
                    "svg-patterns": {},
                    "backgrounds": {}
                },
            },
            
            "tailwind": {},
            "dark-mode": {},
        },
        "application-logic":{
            "hooks": {
                "__files": ["custom-hooks.md", "useMemo.md", "useCallback.md", "useRef.md"]
            },
            "context-api": {
                "__files": ["overview.md", "best-practices.md"]
            },
            "render-props": {},
            "higher-order-components": {},
            "compound-components": {},
            "portals": {},
            "state-management": {
                "context-api": {},
                "zustand": {},
                "jotai": {},
                "redux": {},
                "recoil": {},
                "react-query": {},
                "mobx": {},
                "xstate": {},
                "redux-saga": {},
                "redux-thunk": {},
                "redux-toolkit": {
                    "__files": ["overview.md", "createSlice.md", "createAsyncThunk.md"]
                },
                "zustand-persist": {}
            },
            
            "routing": {
                "react-router": {
                    "__files": ["params.md", "nested.md", "lazy.md", "redirects.md"]
                },
                "nextjs-router": {
                    "__files": ["app-router.md", "pages-router.md", "link-navigation.md"]
                },
                "__files": ["astro-router.md", "patterns.md"]
            },
            "forms-handling": {
                "__files": ["native-forms.md", "best-practices.md"],
                "formik": {},
                "react-hook-form": {
                    "__files": ["useForm.md", "resolver.md"]
                },
                "validation": {
                    "__files": ["yup.md", "zod.md", "compare.md"]
                }
            },
            "data-fetching": {
                "__files": ["fetch-api.md", "axios.md", "comparison.md"],
                "swr": {},
                "react-query": {
                    "__files": ["queries.md", "mutations.md", "cache.md"]
                },
                "tanstack-query": {}
            },
            
            "testing": {
                "__files": ["best-practices.md"],
                "jest": {},
                "vitest": {},
                "testing-library": {
                    "__files": ["queries.md", "events.md"]
                },
                "playwright": {},
                "cypress": {}
            },
            "error-handling": {
                "__files": ["try-catch.md", "error-boundaries.md", "logging.md"]
            },
            "i18n": {
                "__files": ["react-i18next.md", "next-i18next.md"]
            },
            "local-storage": {
                "__files": ["best-practices.md"]
            },
            "websockets": {
                "__files": ["socketio.md", "graphql-subscriptions.md"]
            },
            "type-safety": {
                "__files": ["typescript.md", "flow.md", "prop-types.md"]
            },
        },
    },
    "02_backend": {
        "frameworks": {
            "express": {
                "__files": ["routing.md", "middleware.md", "validation.md", "error-handling.md"]
            },
            "fastify": {},
            "nestjs": {},
            "hapi": {},
            "nodejs": {
                "__files": ["cli.md", "fs.md", "events.md", "streams.md"]
            },
        },
        "databases": {
            "relational": {
                "postgresql": {
                    "__files": ["cli.md", "joins.md", "indexing.md"]
                },
                "mysql": {},
                "sqlite": {},
                "mariadb": {},
            },
            "nosql": {
                "mongodb": {
                    "__files": ["mongoose.md", "aggregation.md", "indexes.md"]
                },
                "redis": {
                    "__files": ["caching.md", "pubsub.md"]
                },
                
            },
            "orm-odm": {
                "prisma": {
                    "__files": ["schema.md", "relations.md", "migrations.md"]
                },
                "mongoose": {
                    "__files": ["schema.md", "relations.md", "migrations.md"]
                },
            },
            
        },
        "architecture": {
            "rest": {
                "__files": ["routing.md", "status-codes.md", "versioning.md"]
            },
            "graphql": {
                "__files": ["queries.md", "mutations.md", "caching.md"]
            },
            "microservices": {
                "__files": ["patterns.md", "service-discovery.md", "messaging.md"]
            },
            "sockets": {
                "socketio": {}
            }
        },
        "security": {
            "auth": {
                "__files": ["jwt.md", "oauth.md", "sessions.md"]
            },
            "cors": {
                "__files": ["config.md"]
            },
            "__files": ["cors.md", "headers.md", "validation.md"]
        },
        "api": {
            "__files": ["versioning.md", "rate-limiting.md", "caching.md"]
        }
    },
    "03_devtools": {
        "editors": {
            "vscode": {
                "__files": ["settings.md", "extensions.md", "snippets.md"]
            },
        },
        "terminals": {
            "__files": ["zsh.md", "bash.md", "aliases.md"]
        },
        "git": {
            "__files": ["cli.md", "branching.md", "hooks.md", "workflows.md", "rebase-vs-merge.md"],
            "github": {
                "__files": ["issues.md", "pull-requests.md", "actions.md"]
            },
        },
        "linters-formatters": {
            "eslint": {},
            "prettier": {},
            "__files": ["stylelint.md", "husky-lintstaged.md"]
        },
        "browsers": {
            "__files": ["devtools.md", "extensions.md"],
            "chrome": {
                "__files": ["devtools.md", "extensions.md"]
            },
            "firefox": {
                "__files": ["devtools.md", "extensions.md"]
            },
            "safari": {
                "__files": ["devtools.md", "extensions.md"]
            },
            "edge": {
                "__files": ["devtools.md", "extensions.md"]
            },
        },
        "package-managers": {
            "__files": ["npm.md", "yarn.md", "pnpm.md", "monorepo.md"],
        },
        "automation": {
            "__files": ["makefile.md", "taskrunners.md", "npx.md"]
        },
        "cli-tools": {
            "__files": ["httpie.md", "curl.md", "fzf.md", "jq.md", "nvm.md"]
        }
    },
    "04_methodologies": {
        "coding-principles": {
            "__files": ["dry.md", "kiss.md", "solid.md", "yagni.md"]
        },
        "css-methodologies": {
            "__files": ["bem.md", "oocss.md", "smacss.md", "itcss.md"]
        },
        "project-structure": {
            "feature-sliced-design": {
                "__files": ["layers.md", "examples.md", "folder-structure.md"]
            },
            "atomic-design": {
                "__files": ["atoms-molecules-organisms.md"]
            },
            "__files": ["component-driven-development.md"]
        },
        "testing": {
            "__files": ["tdd.md", "bdd.md", "integration-vs-unit.md"]
        },
        "state-management-patterns": {
            "__files": ["redux-patterns.md", "observer-pattern.md"]
        },
        "ui-architecture": {
            "__files": ["presentational-vs-container.md", "smart-dumb-components.md"]
        }
    },
    "05_concepts": {
        "web-standards": {
            "__files": ["html-spec.md", "accessibility.md", "w3c-vs-whatwg.md"]
        },
        "protocols": {
            "http": {
                "__files": ["methods.md", "status-codes.md", "headers.md", "caching.md"]
            },
            "websockets": {
                "__files": ["events.md", "use-cases.md"]
            },
            "__files": ["https.md"]
        },
        "browsers": {
            "__files": ["dom.md", "rendering-pipeline.md", "repaint-reflow.md"]
        },
        "javascript-internals": {
            "__files": ["event-loop.md", "call-stack.md", "memory-management.md", "js-engine.md"]
        },
        "performance": {
            "__files": ["async-vs-defer.md", "layout-shifts.md", "lazy-loading.md"]
        },
        "caching-strategies": {
            "__files": ["http-cache.md", "service-workers.md", "swr.md"]
        }
    },
    "06_deployment": {
        "vercel": {
            "__files": ["overview.md", "setup.md", "env-variables.md", "routing.md", "vercel-json.md", "cli.md", "troubleshooting.md"],
            "edge-functions": {
                "__files": ["basics.md", "use-cases.md", "limitations.md"]
            }
        },
        "netlify": {},
        "render": {},
        "docker": {},
        "nginx": {},
        "pm2": {},
        "ci-cd": {},
        "github-actions": {}
    },
    "07_seo-performance": {
        "lighthouse": {
            "__files": ["audit-categories.md", "cli-usage.md", "improvement-tips.md"]
        },
        "core-web-vitals": {
            "__files": ["lcp.md", "cls.md", "fid.md", "web-vitals-library.md"]
        },
        "meta-tags": {
            "__files": ["title-description.md", "og-tags.md", "twitter-cards.md", "favicons.md"]
        },
        "image-optimization": {
            "__files": ["modern-formats.md", "responsive-images.md", "cdn.md", "next-gen-libraries.md"]
        },
        "ssr-ssg": {
            "__files": ["nextjs.md", "astro.md", "nuxt.md"]
        },
        "accessibility": {
            "__files": ["aria.md", "color-contrast.md", "keyboard.md"]
        },
        "performance-optimization": {
            "__files": ["code-splitting.md", "tree-shaking.md", "lazy-loading.md"]
        },
        "analytics": {
            "__files": ["google-analytics.md", "gtag.md", "ga4.md"]
        },
    }
}


import os
from datetime import datetime

BASE_DIR = "./"

def format_index_md(title, related_links):
    date = datetime.now().strftime("%Y-%m-%d")
    related_section = "\n".join([f"- [[{path}|{label}]]" for path, label in related_links])

    return f"""---
title: {title}
created: {date}
tags: []
aliases: []
type: note
status: draft
---

# {title}

## 🧠 Summary

> Briefly describe what this note is about.

## 🔗 Related Notes

{related_section if related_section else "-"}

## 🗂️ Resources / References

- [ ] Add links here
"""

def create_structure(base_path, structure, parent_path=""):
    for name, children in structure.items():
        if name == "__files":
            continue

        path = os.path.join(base_path, name)
        os.makedirs(path, exist_ok=True)

        # Относительный путь к этой папке (в формате Obsidian)
        current_path = os.path.join(parent_path, name).replace("\\", "/")

        # 🔗 Related Notes: подпапки (index.md)
        related_links = []
        for key, val in children.items():
            if key != "__files" and isinstance(val, dict):
                rel_path = os.path.join(current_path, key, "index").replace("\\", "/")
                label = key.replace("-", " ").replace("_", " ").title()
                related_links.append((rel_path, label))

        # 🔗 Related Notes: обычные файлы рядом (overview.md, cli.md и т.п.)
        if "__files" in children:
            for filename in children["__files"]:
                file_path = os.path.join(current_path, filename).replace("\\", "/")
                label = filename.replace(".md", "").replace("-", " ").title()
                related_links.append((file_path, label))

                # файл создаём, если не существует
                full_file_path = os.path.join(path, filename)
                if not os.path.exists(full_file_path):
                    with open(full_file_path, "w", encoding="utf-8") as f:
                        f.write(f"# {label}\n")

        # 📝 index.md создаётся один раз
        index_path = os.path.join(path, "index.md")
        if not os.path.exists(index_path):
            title = name.replace("-", " ").replace("_", " ").title()
            with open(index_path, "w", encoding="utf-8") as f:
                f.write(format_index_md(title, related_links))

        # Рекурсивный обход вложенных структур
        for key, val in children.items():
            if key != "__files" and isinstance(val, dict):
                create_structure(path, {key: val}, os.path.join(parent_path, name))

if __name__ == "__main__":
    print("🚀 Обновление структуры Obsidian Vault...")
    create_structure(BASE_DIR, vault_structure)
    print(f"✅ Готово! Структура создана/обновлена в: {BASE_DIR}/")
