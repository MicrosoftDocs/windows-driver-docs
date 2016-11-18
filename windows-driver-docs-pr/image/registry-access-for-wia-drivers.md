---
title: Registry Access for WIA Drivers
author: windows-driver-content
description: Registry Access for WIA Drivers
MS-HAID:
- 'WIA\_best\_practice\_be148eac-3738-422b-91f1-ad7532ccb171.xml'
- 'image.registry\_access\_for\_wia\_drivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 0e0b7493-858b-4add-9e1d-fd71bae21b6e
---

# Registry Access for WIA Drivers


## <a href="" id="ddk-registry-access-for-wia-drivers-si"></a>


Driver developers should know the permissions for the registry keys they need to access. Much of the registry is available for the driver to read. However, WIA drivers should write only to the registry key handed to them in the [**IStiUSD::Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff543824) method.

Although writing to other registry keys is possible in Windows XP, because the WIA service runs under the high-privilege **LocalSystem** account, this is no longer possible under the low-privilege **LocalService** account in Microsoft Windows Server 2003 and later.

Drivers often need write access to their registry key outside of **IStiUSD::Initialize**. Because most drivers store data in the **DeviceData** subkey, it is easy to open the **DeviceData** subkey and store the handle to the open key to be used later. The driver should close the registry key only when it no longer needs the key.

The following code example illustrates using the **DeviceData** registry subkey.

```
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
      //  Notice that it isn&#39;t closed here, but instead,
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
  // If the writable registry key isn&#39;t closed  yet, do it now,
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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Registry%20Access%20for%20WIA%20Drivers%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


