---
title: Using a Manifest File with SymChk
description: Using a Manifest File with SymChk
ms.assetid: ee5d0c39-1838-4595-adf4-6cd1261a57c8
ms.author: domars
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using a Manifest File with SymChk


## <span id="ddk_using_symchk_dtoolq"></span><span id="DDK_USING_SYMCHK_DTOOLQ"></span>


In some cases, you might need to retrieve symbols for files that are on an isolated computer; that is, a computer that is either not on any network or is on a network that has no symbol store. In that situation, you can use the following procedure to retrieve symbols.

1.  Run SymChk with the **/om** parameter to create a manifest file that describes the files for which you want to retrieve symbols.

2.  Move the manifest file to a network that has a symbol store.

3.  Run SymChk with **/im** parameter to retrieve symbols for the files described int the manifest file.

4.  Move the symbol files back to the isolated computer.

### <span id="example"></span><span id="EXAMPLE"></span>Example

Suppose yourApp.exe is running on an isolated computer. The following command creates a manifest file that describes all the symbols needed to debug the yourApp.exe pocess.

```
C:\>SymChk /om c:\Manifest\man.txt /ie yourApp.exe

SYMCHK: FAILED files = 0
SYMCHK: PASSED + IGNORED files = 28
```

Now assume you have moved the manifest file to a different computer that is on a network that has access to a symbol store. The following command retrieves the symbols described in the manifest file and places them in the mySymbols folder.

```
C:\>SymChk /im c:\FolderOnOtherComputer\man.txt /s srv*c:\mysymbols*\\aServer\symbols

SYMCHK: myApp.exe             ERROR - Unable to download file. Error reported was 2
. . .
SYMCHK: FAILED files = 28
SYMCHK: PASSED + IGNORED files = 28
```

Now you can move the symbols to the isolated computer and use them for debugging.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20a%20Manifest%20File%20with%20SymChk%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




