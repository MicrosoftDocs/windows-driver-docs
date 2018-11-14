---
title: Using a Manifest File with SymChk
description: Using a Manifest File with SymChk
ms.assetid: ee5d0c39-1838-4595-adf4-6cd1261a57c8
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Using a Manifest File with SymChk


## <span id="ddk_using_symchk_dtoolq"></span><span id="DDK_USING_SYMCHK_DTOOLQ"></span>


In some cases, you might need to retrieve symbols for files that are on an isolated computer; that is, a computer that is either not on any network or is on a network that has no symbol store. In that situation, you can use the following procedure to retrieve symbols.

1.  Run SymChk with the **/om** parameter to create a manifest file that describes the files for which you want to retrieve symbols.

2.  Move the manifest file to a network that has a symbol store.

3.  Run SymChk with the **/im** parameter to retrieve symbols for the files described in the manifest file.

4.  Move the symbol files back to the isolated computer.

### <span id="example"></span><span id="EXAMPLE"></span>Example

Suppose yourApp.exe is running on an isolated computer. The following command creates a manifest file that describes all the symbols needed to debug the yourApp.exe pocess.

```dbgcmd
C:\>SymChk /om c:\Manifest\man.txt /ie yourApp.exe

SYMCHK: FAILED files = 0
SYMCHK: PASSED + IGNORED files = 28
```

Now assume you have moved the manifest file to a different computer that is on a network that has access to a symbol store. The following command retrieves the symbols described in the manifest file and places them in the mySymbols folder.

```dbgcmd
C:\>SymChk /im c:\FolderOnOtherComputer\man.txt /s srv*c:\mysymbols*\\aServer\symbols

SYMCHK: myApp.exe             ERROR - Unable to download file. Error reported was 2
. . .
SYMCHK: FAILED files = 28
SYMCHK: PASSED + IGNORED files = 28
```

Now you can move the symbols to the isolated computer and use them for debugging.

 

 





