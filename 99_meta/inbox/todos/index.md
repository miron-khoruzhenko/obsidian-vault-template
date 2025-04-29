---
title: Todos
tags: [overview]
---

# ✅ All ToDo's

> This file gathers all todos from the folder.

## All task files
```dataview
table created as "Created", status
from "99_meta/inbox/todos"
where type = "task-list"
sort created desc
```
## All tasks
```dataview
task
from "99_meta/inbox/todos"
group by file.name
sort created desc
```


