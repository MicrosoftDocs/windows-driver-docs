---
title: 'WinDbg: Keyboard Shortcuts'
description: "This article provides the keyboard shortcuts for the WinDbg debugger."
keywords: ["keyboard shortcuts", "WinDbg", "Menu", "Windows Debugging"]
ms.date: 01/09/2019
ms.topic: checklist
---

# WinDbg keyboard shortcuts

:::image type="content" source="images/windbgx-preview-logo.png" alt-text="WinDbg logo with a magnifying glass inspecting bits.":::

This article summarizes the keyboard shortcuts for WinDbg, the debugger for Windows.

All the ribbon menu options are available by using the Alt key plus the first letter of the option. Examples are Alt+H to go to the **Home** menu and Alt+H+S to stop debugging.

:::image type="content" source="images/windbgx-ribbon-home-menu-alt-keys.png" alt-text="Screenshot of the WinDbg Home menu displaying quick key letters for ribbon options.":::

### Flow control

| Keystroke     | Description             |
| ------------- |-------------------------|
F5 | Continue.
F10     | Step over.
F11     | Step into.
Shift+F11   |   Step out.
F7      | Run to line.
Ctrl+Shift+I    |   Set instruction pointer to highlighted line.
Ctrl+Break or Alt+Del   |   Break.
Ctrl+Shift+F5   |   Restart.
Shift+F5    |   Stop debugging.
Alt+H,D     | Detach.

### Command window

| Keystroke     | Description |
| ------------- | ------------------------- |
Ctrl+M          | Toggle focus between output pane (mark mode) and input box.
Ctrl+Space      | Trigger command completion list pop-up.
Tab             | Trigger next autocompletion.
Shift+Tab       | Trigger previous autocompletion.
Ctrl+F          | Open find box.
↑ / ↓           | Navigate command history.
Shift+↑ / ↓     | Navigate command history matching current text in command input.
Ctrl+[          | Select previous output pane section.
Ctrl+]          | Select next output pane section.

### Setup

| Keystroke     | Description             |
| ------------- |-------------------------|
F6          |       Attach to process.
Ctrl+R      |       Connect to remote.
Ctrl+D      |       Open dump file.
Ctrl+K      |       Attach to kernel debugger.
Ctrl+E      |       Launch process.
Ctrl+P      |       Launch app package.

### Breakpoints

| Keystroke     | Description             |
| ------------- |-------------------------|  
F9              |  Toggle breakpoint on highlighted line.
Ctrl+F9       |  Toggle breakpoint-enabled state on highlighted line.
Shift+F9      |  Add breakpoint.
Ctrl+Alt+K      |  Toggle initial break.

### Windowing

| Keystroke     | Description             |
| ------------- |-------------------------|
Ctrl+Tab        |       Open window changer.
Alt+1           |       Open/focus on **Command** window.
Alt+2           |       Open/focus on **Watch** window.
Alt+3           |       Open/focus on **Locals** window.
Alt+4           |       Open/focus on **Registers** window.
Alt+5           |       Open/focus on **Memory** window.
Alt+6           |       Open/focus on **Stack** window.
Alt+7           |       Open/focus on **Disassembly** window.
Alt+8           |       Open/focus on **Breakpoints** window.
Alt+9           |       Open/focus on **Threads** window.

### Scripting

| Keystroke      | Description             |
| -------------- |-------------------------|
Ctrl+Shift+O     |      Open script.
Ctrl+Shift+Enter |      Execute script.
Ctrl+S           |      Save script.
Alt+S,N          |      New script.
Alt+S,U          |      Unlink script.

### Stack navigation

| Keystroke     | Description             |
| ------------- |-------------------------|
Ctrl+↑ / ↓      |   Move up/down a stack frame.

### Help

| Keystroke     | Description             |
| ------------- |-------------------------|
F1              |       Open help file.
Shift+F1        |       Search selection online (source window).

### Miscellaneous  

| Keystroke     | Description             |
| ------------- |-------------------------|
Ctrl+Alt+V      |       Toggle verbose mode.

## Related content

- [WinDbg features](../debugger/debugging-using-windbg.md)