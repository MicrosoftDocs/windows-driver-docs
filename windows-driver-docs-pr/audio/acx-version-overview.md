---
title: ACX Version Information
description: This topic provides a summary of the ACX and KMDF version information 
ms.date: 03/07/2024
ms.localizationpriority: medium
---

# ACX version information

This topic discusses ACX and KMDF version information. For a general overview of ACX, see [ACX audio class extensions overview](acx-audio-class-extensions-overview.md).

>[!NOTE]
> The ACX headers and libraries are not included in the  WDK 10.0.22621.2428 (released October 24, 2023), but are available in previous versions, as well as the latest (25000 series builds) Insider Preview of the WDK. For more information about preview versions of the WDK, see [Installing preview versions of the Windows Driver Kit (WDK)](../installing-preview-versions-wdk.md).

## ACX and KMDF versions

Use the [!wdfkd.wdfldr](../debuggercmds/-wdfkd-wdfldr.md) extension  to view version information for ACX. The !wdfkd.wdfldr extension displays information about the drivers that are currently dynamically bound to the Windows Driver Frameworks.

```dbgcmd
!wdfkd.wdfldr Acx01000.sys
```

### Version 1.1

The current version of ACX is **1.1** and is recommended for all new driver development.

Windows OS support for ACX versions are described in the following table.

| Operating system         | KMDF version | Supported ACX version | Version notes           |
|--------------------------|--------------|-----------------------|-------------------------|
| Windows 10, version 2004 | Minimum 1.31 | 1.1                   | Initial public release. |

These DDIs were added in version 1.1.

- AcxCircuitGetElementsCount
- AcxCircuitGetPinsCount
- AcxCircuitGetSymbolicLinkName
- AcxCircuitGetNotificationId
- AcxFactoryCircuitGetSymbolicLinkName
- AcxDataFormatListRemoveDataFormats
- AcxPinRemoveModeDataFormatList
- AcxStreamGetElementsCount
- AcxStreamGetNotificationId
- AcxTargetCircuitGetSymbolicLinkName
- AcxTargetPinFlushModeDataFormatListCache

### Pre-release 1.0 version

Version 1.0 is not recommended for new driver development, but it was used in early development and testing of ACX drivers.

| Operating system         | KMDF version | Supported ACX version | Version notes |
|--------------------------|--------------|-----------------------|---------------|
| Windows 10, version 1903 | 1.29         | 1.0                   | Pre-release.  |

## KMDF version information

ACX objects are Windows Driver Framework (WDF) objects - WDFOBJECT. For more information about WDF, see [Introduction to Framework Objects](../wdf/introduction-to-framework-objects.md). ACX binds to a specific version of KMDF at runtime. For more information, see [KMDF Version History](../wdf/kmdf-version-history.md).

For information about installing different versions of WDF/KMDF, see the following topics:

- [Building and Loading a WDF Driver](../wdf/building-and-loading-a-kmdf-driver.md#which-framework-version-should-i-use)

- [Building a WDF driver for multiple versions of Windows](../wdf/building-a-wdf-driver-for-multiple-versions-of-windows.md)

- [Specifying the KMDF Co-installer in an INF File](../wdf/installing-the-framework-s-co-installer.md)

ACX Binds to a specific version of KMDF at runtime. When Windows loads a kernel-mode WDF driver, the driver is dynamically bound to the KMDF run-time library (WdfMM000.sys). Multiple drivers can share the same run-time library (DLL) image, and the run-time libraries for two major versions can co-exist side by side. For information about KMDF versioning, see [Framework Library Versioning](../wdf/framework-library-versioning.md).

## Multiple ACX version support

When you build the audio driver, you specify the maximum and minimum version of the ACX framework you want to use at compilation time. Thus, the audio driver at run time can assume that the max/min version of DDI is available, else the audio driver fails to load.

ACX drivers can be written to run on multiple versions of ACX and at run-time make the call if a specific ACX DDI, structure, etc. is present or not in that version.  **ACX_IS_FUNCTION_AVAILABLE(FunctionName)** can be used to see if a specific function in available in a specific version of ACX. For more information, see [ACX_IS_FUNCTION_AVAILABLE macro](/windows-hardware/drivers/ddi/acxfuncenum/nf-acxfuncenum-acx_is_function_available).

The following code, provides an example on how to check if a function is available.

```cpp
    if (ACX_IS_FUNCTION_AVAILABLE( AcxTargetPinFlushModeDataFormatListCache)) {
        DbgPrint("Available:  AcxTargetPinFlushModeDataFormatListCache\n");
    }
    else
    {
        DbgPrint("Not available:  AcxTargetPinFlushModeDataFormatListCache\n");
        ASSERT(FALSE);
    }
```

Also available are these similar functions.

**ACX_IS_STRUCTURE_AVAILABLE(StructName)** described in [ACX_IS_STRUCTURE_AVAILABLE macro](/windows-hardware/drivers/ddi/acxfuncenum/nf-acxfuncenum-acx_is_structure_available).

**ACX_IS_FIELD_AVAILABLE(StructName, FieldName)** described in [ACX_IS_FIELD_AVAILABLE macro](/windows-hardware/drivers/ddi/acxfuncenum/nf-acxfuncenum-acx_is_field_available).

ACX also supports the [ACX_DRIVER_VERSION_AVAILABLE_PARAMS_INIT function](/windows-hardware/drivers/ddi/acxdriver/nf-acxdriver-acx_driver_version_available_params_init) which can be used to check version information of the audio driver as shown in the following code sample.

```cpp
    ACX_DRIVER_VERSION_AVAILABLE_PARAMS_INIT(&ver, 1, 1);
    if (!AcxDriverIsVersionAvailable(driver, &ver))
    {
        ASSERT(FALSE);
        goto exit;
    } 
```

## See also

[ACX_IS_FUNCTION_AVAILABLE macro](/windows-hardware/drivers/ddi/acxfuncenum/nf-acxfuncenum-acx_is_function_available)

[ACX audio class extensions overview](acx-audio-class-extensions-overview.md)

[ACX reference documentation](acx-reference.md)
