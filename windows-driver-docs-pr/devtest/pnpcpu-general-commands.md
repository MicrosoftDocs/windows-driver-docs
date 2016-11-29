---
title: PNPCPU General Commands
description: PNPCPU General Commands
ms.assetid: 8b98149c-6c5a-4c1f-b988-dce86bdc3e29
keywords: ["PNPCPU WDK , commands"]
---

# PNPCPU General Commands


The following syntax is common for all PNPCPU operations.

```
pnpcpu.exe -operation
```

### <span id="parameters"></span><span id="PARAMETERS"></span>Parameters

<span id="-install"></span><span id="-INSTALL"></span>**-install**  
Installs the tool on the local computer.

<span id="-uninstall"></span><span id="-UNINSTALL"></span>**-uninstall**  
Removes the tool from the local computer, and returns the computer to the state it was in before running **-install**.

This includes clearing all processor error codes that could be observed after the **-install** command was run and the system was restarted.

<span id="-add"></span><span id="-ADD"></span>**-add**  
Performs a hot-add operation on every logical processor in the system, up to the maximum supported by the license.

<span id="-__or_-help"></span><span id="-__OR_-HELP"></span>**-?** or **-help**  
Displays usage information similar to this documentation.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

There are no further optional parameters for any of the commands listed.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20PNPCPU%20General%20Commands%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




