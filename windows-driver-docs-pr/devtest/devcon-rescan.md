---
title: DevCon Rescan
description: Uses Windows Plug and Play features to update the device list for the computer. Valid on local and remote computers.
ms.assetid: 08762f30-a276-4ef4-8936-dfb1e1f692ca
keywords: ["DevCon Rescan Driver Development Tools"]
topic_type:
- apiref
api_name:
- DevCon Rescan
api_type:
- NA
---

# DevCon Rescan


Uses Windows Plug and Play features to update the device list for the computer. Valid on local and remote computers.

``` syntax
    devcon [/m:\\computer] [/r] rescan 

   
```

## <span id="ddk_devcon_rescan_tools"></span><span id="DDK_DEVCON_RESCAN_TOOLS"></span>Parameters


<span id="________m___computer______"></span><span id="________M___COMPUTER______"></span> **/m:\\\\***computer*   
Runs the command on the specified remote computer. The backslashes are required.

**Note**   To run DevCon commands on a remote computer, the Group Policy setting must allow the Plug and Play service to run on the remote computer. On computers that run Windows Vista and Windows 7, the Group Policy disables remote access to the service by default. On computers that run WDK 8.1 and WDK 8, the remote access is unavailable.

 

<span id="________r______"></span><span id="________R______"></span> **/r**   
Conditional reboot. Reboots the system after completing an operation only if a reboot is required to make a change effective.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The **/m** parameter must precede the operation name (**rescan**). Otherwise, DevCon ignores the **/m** parameter and scans the local computer without returning a syntax error.

Rescanning can cause the Plug and Play manager to detect new devices and to install device drivers without warning.

Rescanning can detect some non-Plug and Play devices, particularly those that cannot notify the system when they are installed, such as parallel-port devices and serial-port devices. As a result, you must have Administrator privileges to run **DevCon Rescan** commands.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon rescan
devcon /m:\\Server01 rescan
```

### <span id="example"></span><span id="EXAMPLE"></span>Example

[Example 37: Scan the computer for new devices](devcon-examples.md#ddk_example_37_scan_the_computer_for_new_devices_tools)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20DevCon%20Rescan%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




