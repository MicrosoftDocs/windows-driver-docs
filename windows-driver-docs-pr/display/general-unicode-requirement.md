---
title: General Unicode Requirement in INF Files
description: INF files should generally be saved and encoded as Unicode.
ms.date: 05/23/2024
ms.topic: concept-article
---

# General Unicode requirement in INF files

INF files must be saved with Unicode (UTF-16 LE) or ANSI file encoding. Unicode (UTF-16 LE) is preferred since it allows the INF to support localizing the INF Strings section in a wide variety of languages. If your INF contains non-ASCII characters, you must save the file as a Unicode (UTF-16 LE) file.

You can create or modify an INF file by using any text editor in which you can control the insertion of line breaks.

To check for Unicode in INF files using Notepad:

1. Use Notepad to open the INF file.
2. On the **File** menu, select **Save As**.
3. If **ANSI** appears in the **Encoding** field of the dialog box, change the encoding to **UTF-16 LE** (**Unicode** on older versions of Notepad) and save the file under a new name.

The following figure shows the **Save As** dialog box for a file that has ANSI encoding:

:::image type="content" source="images/saveasdialogansi.jpg" alt-text="Screenshot of Save As dialog box with ANSI encoding selected.":::

The proper default value is shown in this figure:

:::image type="content" source="images/saveasdialogutf16le.jpg" alt-text="Screenshot of Save As dialog box with UTF-16 LE encoding selected.":::

On older versions of Notepad, it might look like this figure:

:::image type="content" source="images/saveasdialogunicode.jpg" alt-text="Screenshot of Save As dialog box with Unicode encoding selected on older Notepad versions.":::
