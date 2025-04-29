<%*
const isIndex = tp.file.title === "index";
const rawName = isIndex
  ? tp.file.folder(true).split("/").pop()
  : tp.file.title;

const title = rawName.charAt(0).toUpperCase() + rawName.slice(1);
tR += `---
title: ${title}
created: ${tp.date.now("YYYY-MM-DD")}
tags: []
aliases: []
type: note
status: draft
---

# ${title}

## 🧠 Summary

> Briefly describe what this note is about.

## 🔗 Related Notes

- 

## 🗂️ Resources / References

- [ ] Add links here
`;
%>

## 🧑‍🤝‍🧑 Meeting Info

- **Date:** <% tp.date.now("YYYY-MM-DD") %>
- **Participants:** 
- **Location / Platform:** Zoom / Discord / etc.

---

## 🧵 Agenda

- [ ] Topic 1
- [ ] Topic 2
- [ ] Topic 3

---

## 🗣️ Discussion Summary

> Summarize the key discussions that took place.

---

## ✅ Decisions / Outcomes

- Decision 1
- Decision 2

---

## 🔜 Action Items

- [ ] Task 1 assigned to Person A
- [ ] Task 2 assigned to Person B
