---
title: Registry Access for WIA Drivers
description: Registry Access for WIA Drivers
ms.assetid: 0e0b7493-858b-4add-9e1d-fd71bae21b6e
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registry Access for WIA Drivers





Driver developers should know the permissions for the registry keys they need to access. Much of the registry is available for the driver to read. However, WIA drivers should write only to the registry key handed to them in the [**IStiUSD::Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff543824) method.

Although writing to other registry keys is possible in Windows XP, because the WIA service runs under the high-privilege **LocalSystem** account, this is no longer possible under the low-privilege **LocalService** account in Microsoft Windows Server 2003 and later.

Drivers often need write access to their registry key outside of **IStiUSD::Initialize**. Because most drivers store data in the **DeviceData** subkey, it is easy to open the **DeviceData** subkey and store the handle to the open key to be used later. The driver should close the registry key only when it no longer needs the key.

The following code example illustrates using the **DeviceData** registry subkey.

```cpp
STDMETHODIMP CWIADevice::Initialize(
  PSTIDEVICECONTROL   pIStiDevControl,
  DWORD               dwStiVersion,
  HKEY                hParametersKey)
{
  .
  .
  .
  //
  // Open the DeviceData key since this is where the
  // driver-specific settings will be stored.
  //
  DWORD dwError = RegOpenKeyEx(
                 hParametersKey,     // handle to open key
                 TEXT("DeviceData"), // subkey to open
                 0,                  // options (must be NULL)
                 KEY_READ|KEY_WRITE, // requesting read/write access
                 &m_hMyWritableRegistryKey);
  if (dwError == ERROR_SUCCESS)
  {
      //
      //  m_hMyWritableRegistryKey now contains a handle to the
      //  DeviceData subkey which can be used to store information
      //  in the registry.
      //  Notice that it isn't closed here, but instead,
      //  kept open because it is needed later.
     //
  }
  else 
  {
      // Handle error
      .
      .
      .
  }
  .
  .
  .
}

STDMETHODIMP CWIADevice::SomeDriverMethod()
{
  .
  .
  .
  //
  //  We need to store some setting in the registry here.
  //
  DWORD dwError = RegSetValueEx(
                     m_hMyWritableRegistryKey,
                     TEXT("MyDriverValueName"),
                     0,
                     REG_DWORD,
                     (BYTE*)&dwValue,
                     sizeof(dwValue));
  if (dwError == ERROR_SUCCESS)
  {
      //
      //  We successfully stored dwValue in the registry
      //
  }
  else 
  {
      // Handle error
      .
      .
      .
  }
  .
  .
  .
}

CWIADevice:: CWIADevice () :
  m_hMyWritableRegistryKey(NULL),
  .
  .
  .
{
  //  Rest of constructor goes here.  Ensure that the
  //   handle to the registry key is initialized to NULL.
}

CWIADevice::~CWIADevice(void)
{
  .
  .
  .
  //
  // If the writable registry key isn't closed  yet, do it now,
  // because the driver is about to be unloaded.
  //
  if (m_hMyWritableRegistryKey) 
  {
      RegCloseKey(m_hMyWritableRegistryKey);
      m_hMyWritableRegistryKey = NULL;
  }

  .
  .
  .
}
```

The **DeviceData** registry subkey is open for read/write access to the driver on Windows Me, and Windows XP and later. The device key itself (for example, the parent registry key to **DeviceData**) may or may not be open for write access by the driver, depending on the operating system version.

**Note**   The driver *must* close any registry keys it opened when they are no longer needed, and must close all registry keys prior to unloading.

 

 

 




