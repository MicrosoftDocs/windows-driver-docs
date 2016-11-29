---
title: PnPUtil Command Syntax
description: To run PnPUtil, open a Command Prompt window (Run as Administrator) and type a command using the following syntax and parameters.Note  PnPUtil (PnPUtil.exe) is included in every version of Windows, starting with Windows Vista (in the windir \\system32 directory). �
ms.assetid: f14ceb98-8d82-43dd-b06e-2595b59b6999
keywords: ["PnPUtil Command Syntax Driver Development Tools"]
topic_type:
- apiref
api_name:
- PnPUtil
api_type:
- NA
---

# PnPUtil Command Syntax


To run PnPUtil, open a Command Prompt window (**Run as Administrator**) and type a command using the following syntax and parameters.

**Note**  PnPUtil (PnPUtil.exe) is included in every version of Windows, starting with Windows Vista (in the %windir%\\system32 directory).

 

``` syntax
    PnPUtil [/a [/i] InfFileName] [/d [/f] PublishedInfFileName] [/e] [/?] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="________a______"></span><span id="________A______"></span> **/a**   
Adds a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) to the [driver store](https://msdn.microsoft.com/library/windows/hardware/ff544868). The *InfFileName* parameter specifies the path and name of the [INF file](https://msdn.microsoft.com/library/windows/hardware/ff547402) in the driver package. For more information about this parameter, see the [Comments](#comments) section later in this topic.

The **/a** switch has the following optional parameters:

<span id="_i"></span><span id="_I"></span>/i  
Installs the [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) on matching devices that are connected to the system. The driver package is installed after it is added to the [driver store](https://msdn.microsoft.com/library/windows/hardware/ff544868).

**Note**  When you add a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) to the [driver store](https://msdn.microsoft.com/library/windows/hardware/ff544868) by using the **/a** switch, Windows uses a different name (*published name*) for the driver package's [INF file](https://msdn.microsoft.com/library/windows/hardware/ff547402). You must use the published name of the INF file for the *PublishedInfFileName* parameter of the **/d** switch.

 

<span id="________d______"></span><span id="________D______"></span> **/d**   
Removes a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) from the [driver store](https://msdn.microsoft.com/library/windows/hardware/ff544868). The *PublishedInfFileName* parameter specifies the published name of the [INF file](https://msdn.microsoft.com/library/windows/hardware/ff547402) for the driver package that was added to the driver store. For more information about this parameter, see the [Comments](#comments) section later in this topic.

The **/d** switch has the following optional parameters:

<span id="_f"></span><span id="_F"></span>/f  
Forces the deletion of the specified [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) from the [driver store](https://msdn.microsoft.com/library/windows/hardware/ff544868). You must use this parameter if the specified driver package is installed on a device that is connected to the system. If this parameter is not specified, PnPUtil only removes a driver package if it was not used to install drivers for devices that are connected to the system.

**Note**  Removing the driver package in this manner will not affect the operation of currently connected devices for which drivers were previously installed from the package.

 

<span id="________e______"></span><span id="________E______"></span> **/e**   
Enumerates the [driver packages](https://msdn.microsoft.com/library/windows/hardware/ff544840) that are currently in the [driver store](https://msdn.microsoft.com/library/windows/hardware/ff544868). Only driver packages that are not in-box packages are listed. An *in-box* driver package is one which is included in the default installation of Windows or its service packs.

<span id="_______________"></span> **/?**   
Displays the command-line syntax.

### <span id="comments"></span><span id="COMMENTS"></span> Comments

The *InfFileName* parameter of the **/a** switch is used to specify the name of [driver package's](https://msdn.microsoft.com/library/windows/hardware/ff544840)[INF file](https://msdn.microsoft.com/library/windows/hardware/ff547402). This parameter has the following syntax:

\[**Drive:\\**\]\[**Path**\]*Filename*

*Filename* can specify one of the following:

-   The name of a single [INF file](https://msdn.microsoft.com/library/windows/hardware/ff547402).
-   The names of all INF files or only specific INF files by using the asterisk ('\*') or question mark ('?') wildcard characters.

If you delete a driver package by using the **/d** switch, you must specify the published name of the INF file through the *PublishedInfFileName* parameter. You can obtain this name through one of the following methods:

-   When the driver package is added to the driver store through the **/a** switch, PnPUtil displays the published name of the INF file for the driver package within the [driver store](https://msdn.microsoft.com/library/windows/hardware/ff544868).
-   Run PnPUtil and use the **/e** switch to list all the driver packages, together with the published names of their INF files, that are currently within the driver store.
    ```
    C:\>pnputil /e
    Microsoft PnP Utility

    Published name : oem0.inf
    Driver package provider : Microsoft
    Class : Printers
    Driver version and date : Unknown driver version and date
    Signer name : microsoft windows

    Published name : oem22.inf
    Driver package provider : Fabrikam, Inc.
    Class : Network adapters
    Driver version and date : 10/07/2009 1.0.200.0
    Signer name : microsoft windows hardware compatibility publisher
    ```

    For examples of how to use the PnPUtil tool, see [PnPUtil Examples](pnputil-examples.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20PnPUtil%20Command%20Syntax%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




