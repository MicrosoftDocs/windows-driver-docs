---
title: DevCon Dp\_add
description: Adds a third-party (OEM) driver package to the driver store on the local computer.
ms.assetid: 929bb59b-f227-47c5-9351-270ffbe4d745
keywords: ["DevCon Dp_add Driver Development Tools"]
topic_type:
- apiref
api_name:
- DevCon Dp_add
api_type:
- NA
---

# DevCon Dp\_add


Adds a third-party (OEM) driver package to the driver store on the local computer.

``` syntax
    devcon dp_add inf

   
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______inf______"></span><span id="_______INF______"></span> *inf*   
The fully qualified path and name of the INF file for the driver package.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

A DevCon dp\_add command copies the specified INF file to the %windir%/Inf directory and renames it OEM\*.inf. This file name is unique on the computer and you cannot specify it.

If this INF file already exists in %windir%/Inf (as determined by comparing the binary files, not by matching the file names) and the catalog (.cat) file for the INF is identical to a catalog file in the directory, the INF file is not recopied to the %windir%/Inf directory.

This command calls the **SetupCopyOEMInf** function with no *CopyStyle* flags. **SetupCopyOEMInf** is described in the Microsoft Windows SDK documentation.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon dp_add C:\WinDDK\5322\src\general\toaste
r\inf\i386\toaster.inf
```

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

[Example 45: Add and Remove Driver Packages](example-45--add-and-remove-driver-packages.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20DevCon%20Dp_add%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




