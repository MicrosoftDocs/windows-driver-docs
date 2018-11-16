---
title: Plug and Play Registry Routines
description: Plug and Play Registry Routines
ms.assetid: d526af4e-8b33-46fb-9af9-b0d9b9f1913a
keywords: ["registry WDK kernel , Plug and Play", "driver registry information WDK kernel , Plug and Play", "Plug and Play WDK kernel , registry routines", "hardware keys WDK kernel", "software keys WDK kernel", "IoOpenDeviceRegistryKey", "IoOpenDeviceInterfaceRegistryKey", "PnP WDK kernel , registry routines"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Plug and Play Registry Routines


The Plug and Play manager associates certain registry keys with a driver, its devices, and its device interface instances. Drivers can use these keys to store persistent properties associated with the driver, or with particular devices or device interface instances.

Drivers must never access these keys directly. Future versions of Windows may store the information at a different location in the registry, or outside the registry entirely. Drivers must not directly access any keys in the following trees:

-   HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class

-   HKLM\\SYSTEM\\CurrentControlSet\\Control\\DeviceClasses

-   HKLM\\SYSTEM\\CurrentControlSet\\Enum

-   HKLM\\SYSTEM\\CurrentControlSet\\Hardware Profiles

Instead, drivers use the [**IoOpenDeviceRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff549443) and [**IoOpenDeviceInterfaceRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff549433) routines to access its PnP keys.

The PnP manager assigns one key for the driver, known as the driver's software key, and a key for each device, known as the device's hardware key. The **IoOpenDeviceRegistryKey** routine can be used to open either key. The value of the *DevInstKeyType* parameter determines which key to open. Specify PLUGPLAY\_REGKEY\_DRIVER to open a software key, or PLUGPLAY\_REGKEY\_DEVICE to a hardware key. The *DeviceObject* parameter specifies the device or driver. (The driver can also access its hardware and software keys relative to the current hardware profile, by ANDing PLUGPLAY\_REGKEY\_CURRENT\_HWPROFILE to *DevInstKeyType*.)

**IoOpenDeviceInterfaceRegistryKey** opens the key associated with a particular device interface instance. The instance is identified by its name, which is a [**UNICODE\_STRING**](https://msdn.microsoft.com/library/windows/hardware/ff564879) returned by [**IoGetDeviceInterfaces**](https://msdn.microsoft.com/library/windows/hardware/ff549186), [**IoGetDeviceInterfaceAlias**](https://msdn.microsoft.com/library/windows/hardware/ff549180), or [**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506). The string is passed as the *SymbolicLinkValue* parameter to **IoOpenDeviceInterfaceRegistryKey**.

These keys can also be set in an INF file, or by using the **SetupDi*Xxx*** routines. For more information, see [Registry Keys for Drivers](https://msdn.microsoft.com/library/windows/hardware/ff549538).

Both [**IoOpenDeviceRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff549443) and [**IoOpenDeviceInterfaceRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff549433) provide an open key handle, with access rights as specified by the *DesiredAccess* parameter. The driver subsequently uses the **Zw*Xxx*** registry routines, such as [**ZwQueryValueKey**](https://msdn.microsoft.com/library/windows/hardware/ff567069) and [**ZwSetValueKey**](https://msdn.microsoft.com/library/windows/hardware/ff567109), to access and manipulate the key. After the driver is no longer using the handle, the driver closes the handle by calling [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417). For more information, see [Using a Handle to a Registry-Key Object](using-a-handle-to-a-registry-key-object.md).

The following code sample demonstrates using **IoOpenDeviceRegistryKey** and **ZwSetValueKey** to set the data associated with the value named "Value" under the device's hardware key.

```cpp
PDEVICE_OBJECT pDeviceObject; // A pointer to the PDO for the device.
HANDLE handle;
UNICODE_STRING ValueName;
ULONG Value = 109; // This is the value we&#39;re setting the key to.
NTSTATUS status;

RtlInitUnicodeString(&ValueName, L"Value");

status = IoOpenDeviceRegistryKey(pDeviceObject, PLUGPLAY_REGKEY_DEVICE, KEY_READ, &handle);

if (NTSUCCESS(status)) {
  status = ZwSetValueKey(handle, ValueName, 0, REG_DWORD, &Value, sizeof(ULONG));
  if (NTSUCCESS(status) {
    ZwClose(handle);
  } else {
    // Handle error.
  }
  // Handle error.
}
```

Note that access to a registry key can be restricted, so a call to [**IoOpenDeviceRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff549443) and [**IoOpenDeviceInterfaceRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff549433) should specify the minimum rights necessary for *DesiredAccess*. If the driver requests an access right that is not allowed, either routine returns STATUS\_ACCESS\_DENIED. In particular, drivers should not specify KEY\_ALL\_ACCESS.

 

 




