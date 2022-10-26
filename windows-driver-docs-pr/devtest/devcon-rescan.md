---
title: DevCon Rescan
description: Uses Windows Plug and Play features to update the device list for the computer. 
keywords:
- DevCon Rescan Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Rescan
api_type:
- NA
ms.date: 10/26/2022
---

# DevCon Rescan

> [!NOTE] 
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available. Its use is recommended instead of DevCon. See the [Recommended Replacement](#recommended-replacement) below and [Replacing DevCon](devcon-migration.md) for more information.

Uses Windows Plug and Play features to update the device list for the computer. 

```
    devcon [/r] rescan 
```

## <span id="ddk_devcon_rescan_tools"></span><span id="DDK_DEVCON_RESCAN_TOOLS"></span>Parameters

<span id="________r______"></span><span id="________R______"></span> **/r**   
Conditional reboot. Reboots the system after completing an operation only if a reboot is required to make a change effective.

## Recommended Replacement

```
pnputil /scan-devices
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## <span id="comments"></span><span id="COMMENTS"></span>Comments

Rescanning can cause the Plug and Play manager to detect new devices and to install device drivers without warning.

Rescanning can detect some non-Plug and Play devices, particularly those that cannot notify the system when they are installed, such as parallel-port devices and serial-port devices. As a result, you must have Administrator privileges to run **DevCon Rescan** commands.

## <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon rescan
```

## <span id="example"></span><span id="EXAMPLE"></span>Example

[Example 37: Scan the computer for new devices](devcon-examples.md#example-37-scan-the-computer-for-new-devices)









