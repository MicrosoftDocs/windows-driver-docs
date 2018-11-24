---
title: Installing a Biometric Driver
description: Installing a Biometric Driver
ms.assetid: f1ae7346-c55b-484e-a94a-b4e22f5fafed
keywords:
- biometric drivers WDK , installing
- installing biometric drivers WDK biometric
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a Biometric Driver


Vendors can provide an INF file to install a WBDI driver.

The following is a list of guidelines for biometric device installation. The code examples in this topic are taken from the WudfBioUsbSample.inx file of the [WudfBioUsbSample](https://github.com/Microsoft/Windows-driver-samples/tree/master/biometrics/driver):

-   WBDI drivers should specify a class of "Biometric." Set ClassGuid equal to the value that corresponds to GUID\_DEVCLASS\_BIOMETRIC in Devguid.h:

    ```cpp
    [Version]
    Signature="$Windows NT$"
    Class=Biometric
    ClassGuid={53D29EF7-377C-4D14-864B-EB3A85769359}
    ```

-   In your .HW section, provide AddReg directives to specify three sections that contain entries to be added to the registry:

    ```cpp
    [Biometric_Install.NT.hw]
    AddReg=Biometric_Device_AddReg
    AddReg=DriverPlugInAddReg, DatabaseAddReg
    ```

-   Provide the named sections referred to in the .HW section. The \[Biometric\_Device\_AddReg\] section sets values for the biometric device, including the exclusive flag and system wake/device idle. To be recognized by Windows Biometric Framework, UMDF-based WBDI drivers must set the "Exclusive" value to 1. The first two lines of the \[Biometric\_Device\_AddReg\] section specify access control list (ACL) rights so that the device can only be opened by an administrator or the local system account. When you specify these ACL rights, third-party applications cannot open the device and capture fingerprint data when the WinBio service is not running. For example:

    ```cpp
    [Biometric_Device_AddReg]
    HKR,,"DeviceCharacteristics",0x10001,0x0100     ; Use same security checks on relative opens
    HKR,,"Security",,"D:P(A;;GA;;;BA)(A;;GA;;;SY)"  ; Allow generic-all access to Built-in administrators and Local system
    HKR,,"LowerFilters",0x00010008,"WinUsb" ; FLG_ADDREG_TYPE_MULTI_SZ | FLG_ADDREG_APPEND
    HKR,,"Exclusive",0x10001,1
    HKR,,"SystemWakeEnabled",0x00010001,1
    HKR,,"DeviceIdleEnabled",0x00010001,1
    HKR,,"UserSetDeviceIdleEnabled",0x00010001,1
    HKR,,"DefaultIdleState",0x00010001,1
    HKR,,"DefaultIdleTimeout",0x00010001,5000
    ```

    A WBDI driver that exposes functionality to a legacy (non-WBDI) biometric stack should set the Exclusive value to zero. If this value is set to zero, the Windows Biometric Framework does not attempt to control the device and the device is not exposed through WBF.

    Vendors can have a single driver binary that can work with legacy stacks and WBF, but the two cannot operate simultaneously. WBF will only operate if the device can be opened with exclusive access.

-   The second named section contains registry values for the plug-in adapters. The sample uses the Microsoft-provided sensor adapter and storage adapter. This section also enables Windows log-in support by setting the SystemSensor value:

    ```cpp
    [DriverPlugInAddReg]
    HKR,WinBio\Configurations,DefaultConfiguration,,"0"
    HKR,WinBio\Configurations\0,SensorMode,0x10001,1                                ; Basic - 1, Advanced - 2
    HKR,WinBio\Configurations\0,SystemSensor,0x10001,1                              ; UAC/Winlogon - 1
    HKR,WinBio\Configurations\0,SensorAdapterBinary,,"WinBioSensorAdapter.DLL"      ; Windows built-in WBDI sensor adapter.
    HKR,WinBio\Configurations\0,EngineAdapterBinary,,"EngineAdapter.DLL"            ; Vendor engine
    HKR,WinBio\Configurations\0,StorageAdapterBinary,,"WinBioStorageAdapter.DLL"    ; Windows built-in storage adapter
    HKR,WinBio\Configurations\0,DatabaseId,,"6E9D4C5A-55B4-4c52-90B7-DDDC75CA4D50"  ; Unique database GUID
    ```

-   Finally, the third section sets the following registry values for the database service. The identifying GUID must be unique for each vendor database of a certain format. For instance, in this code example from the sample, change 6E9D4C5A-55B4-4c52-90B7-DDDC75CA4D50 to your own unique GUID in your INF file.

    ```cpp
    [DatabaseAddReg]
    HKLM,System\CurrentControlSet\Services\WbioSrvc\Databases\{6E9D4C5A-55B4-4c52-90B7-DDDC75CA4D50},BiometricType,0x00010001,0x00000008
    HKLM,System\CurrentControlSet\Services\WbioSrvc\Databases\{6E9D4C5A-55B4-4c52-90B7-DDDC75CA4D50},Attributes,0x00010001,0x00000001
    HKLM,System\CurrentControlSet\Services\WbioSrvc\Databases\{6E9D4C5A-55B4-4c52-90B7-DDDC75CA4D50},Format,,"00000000-0000-0000-0000-000000000000"
    HKLM,System\CurrentControlSet\Services\WbioSrvc\Databases\{6E9D4C5A-55B4-4c52-90B7-DDDC75CA4D50},InitialSize,0x00010001,0x00000020
    HKLM,System\CurrentControlSet\Services\WbioSrvc\Databases\{6E9D4C5A-55B4-4c52-90B7-DDDC75CA4D50},AutoCreate,0x00010001,0x00000001
    HKLM,System\CurrentControlSet\Services\WbioSrvc\Databases\{6E9D4C5A-55B4-4c52-90B7-DDDC75CA4D50},AutoName,0x00010001,0x00000001
    HKLM,System\CurrentControlSet\Services\WbioSrvc\Databases\{6E9D4C5A-55B4-4c52-90B7-DDDC75CA4D50},FilePath,,""
    HKLM,System\CurrentControlSet\Services\WbioSrvc\Databases\{6E9D4C5A-55B4-4c52-90B7-DDDC75CA4D50},ConnectionString,,""
    ```

-   To differentiate WBDI and legacy drivers, vendors must set a Feature Score for the driver in the INX file. Feature Score is not set in the [WudfBioUsbSample](https://github.com/Microsoft/Windows-driver-samples/tree/master/biometrics/driver) sample. For more information about setting a Feature Score, see [Ranking a Biometric Driver on Windows Update](ranking-a-biometric-driver-on-windows-update.md).

For information about INX files and how they differ from INF files, see [Using INX Files to Create INF Files](https://msdn.microsoft.com/library/windows/hardware/ff545473).

In order to replace a WBDI driver with a legacy driver, use the following procedure:

1.  Close all currently active WBF applications.

2.  Uninstall the WBDI driver.

3.  Stop the WBF service, restart it, and then stop it again.

4.  Install the legacy driver.

 

 





