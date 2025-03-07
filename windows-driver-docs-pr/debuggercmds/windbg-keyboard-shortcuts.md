---
title: "WinDbg - keyboard shortcuts"
description: "This section provides the keyboard shortcuts for the WinDbg debugger."
keywords: ["keyboard shortcuts", "WinDbg", "Menu", "Windows Debugging"]
ms.date: 01/09/2019
---

# WinDbg keyboard shortcuts

:::image type="content" source="images/windbgx-preview-logo.png" alt-text="WinDbg logo with a magnifying glass inspecting bits.":::

This section summarizes the keyboard shortcuts for the  WinDbg debugger.

All of the ribbon menu options are available using the **Alt +** the first letter of the option. For example **Alt + H** to go to the home menu, **Alt + H + S** to stop debugging.

:::image type="content" source="images/windbgx-ribbon-home-menu-alt-keys.png" alt-text="Screenshot of WinDbg home menu displaying quick key letters for ribbon options.":::

### Flow control

| Keystroke     | Description             |
| ------------- |-------------------------|
F5 | Continue
F10     | Step over
F11     | Step Into
Shift+F11   |   Step out
F7      | Run to line
Ctrl+Shift+I    |   Set instruction pointer to highlighted line
Ctrl+Break or Alt+Del   |   Break
Ctrl+Shift+F5   |   Restart
Shift+F5    |   Stop debugging
Alt+H,D     | Detach

### Command Window

| Keystroke     | Description |
| ------------- | ------------------------- |
Ctrl+M          | Toggle focus between output pane (mark mode) and input box
Ctrl+Space      | Trigger command completion list popup
TAB             | Trigger next autocompletion
Shift+TAB       | Trigger previous autocompletion
Ctrl+F          | Open find box
↑ / ↓           | Navigate command history
Shift+↑ / ↓     | Navigate command history matching current text in command input
Ctrl+[          | Select previous output pane section
Ctrl+]          | Select next output pane section

### Setup

| Keystroke     | Description             |
| ------------- |-------------------------|
F6          |   Attach to process
Ctrl+R      |       Connect to remote
Ctrl+D      |       Open dump file
Ctrl+K      |       Attach to kernel debugger
Ctrl+E      |       Launch process
Ctrl+P      |       Launch app package

### Breakpoints

| Keystroke     | Description             |
| ------------- |-------------------------|  
F9              |  Toggle breakpoint on highlighted line
Ctrl + F9       |  Toggle breakpoint enabled state on highlighted line
Shift + F9      |  Add breakpoint
Ctrl+Alt+K      |  Toggle initial break

### Windowing

| Keystroke     | Description             |
| ------------- |-------------------------|
Ctrl+Tab        |       Open window changer
Alt+1           |       Open/focus on command window
Alt+2           |       Open/focus on watch window
Alt+3           |       Open/focus on locals window
Alt+4           |       Open/focus on registers window
Alt+5           |       Open/focus on memory window
Alt+6           |       Open/focus on stack window
Alt+7           |       Open/focus on disassembly window
Alt+8           |       Open/focus on breakpoints window
Alt+9           |       Open/focus on thread window

### Scripting

| Keystroke      | Description             |
| -------------- |-------------------------|
Ctrl+Shift+O     |      Open script
Ctrl+Shift+Enter |      Execute script
Ctrl+S           |      Save script
Alt+S,N          |      New script
Alt+S,U          |      Unlink script

### Stack navigation

| Keystroke     | Description             |
| ------------- |-------------------------|
Ctrl+↑ / ↓      |   Move up/down a stack frame

### Help

| Keystroke     | Description             |
| ------------- |-------------------------|
F1              |       Open help file
Shift+F1        |       Search selection online (source window)

### Misc.  

| Keystroke     | Description             |
| ------------- |-------------------------|
Ctrl+Alt+V      |       Toggle Verbose Mode

## See Also

[WinDbg Features](../debugger/debugging-using-windbg.md)

