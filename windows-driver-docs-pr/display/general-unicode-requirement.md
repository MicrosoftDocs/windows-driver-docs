---
title: General Unicode requirement in INF files
description: INF files should be saved and encoded as Unicode; they must not be ANSI.
ms.assetid: 100F5DAB-FD25-4B42-8E3B-321E96CD25A2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# General Unicode requirement in INF files


INF files should be saved and encoded as Unicode (UTF-16); they must not be ANSI or UTF-8.

**To check for Unicode in INF files**

1.  Use Microsoft Notepad to open the INF file.
2.  On the **File** menu, click **Save As**.
3.  If **ANSI** appears in the **Encoding** field of the dialog box, change the encoding to **Unicode** and save the file under a new name.

This figure shows the **Save As** dialog box for a file that has ANSI encoding:

![save as dialog box that has ansi encoding](images/saveasdialogansi.jpg)

The proper default value is shown in this figure:

![save as dialog box that has unicode encoding](images/saveasdialogunicode.jpg)

 

 





