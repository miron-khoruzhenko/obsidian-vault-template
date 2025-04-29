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
