---
title: Loading and Unloading a WIA Minidriver
description: Loading and Unloading a WIA Minidriver
ms.assetid: a5f930c3-f92c-498a-a334-b5eb60fbd61b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Loading and Unloading a WIA Minidriver





After the WIA device driver is installed, the WIA service attempts to load it for the first time. The WIA minidriver's [**IStiUSD::Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff543824) method is called and should perform the following tasks:

1.  Check the transfer mode to determine the caller's intent for initializing this device driver. This is done by calling the [**IStiDeviceControl::GetMyDeviceOpenMode**](https://msdn.microsoft.com/library/windows/hardware/ff542942) method.

2.  Obtain the installed device's port name, so that this driver can call [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) (documented in the Microsoft Windows SDK) on the proper port to access the device. This is done by calling the [**IStiDeviceControl::GetMyDevicePortName**](https://msdn.microsoft.com/library/windows/hardware/ff542944) method.

3.  Read device-specific registry settings written during device installation. This can be done by using *hParametersKey* parameter passed to **IStiUSD::Initialize**.

The WIA service calls the **IStiUSD::Initialize** method when the driver is first loaded. The **IStiUSD::Initialize** method is also called when a client uses the legacy STI DDIs and calls the [**IStillImage::CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff543778) method.

The **IStiUSD::Initialize** method should initialize the WIA driver and the device for use. WIA drivers can store the **IStiDeviceControl** interface pointer if they need it at a later time. The [**IStiDeviceControl::AddRef**](https://msdn.microsoft.com/library/windows/hardware/ff542933) method must be called before storing this interface. If you do not need to store the interface, then ignore it. Do *not* release the **IStiDeviceControl** interface if you have not called **IStiDeviceControl::AddRef** first. This might cause unpredictable results. The [IStiDeviceControl COM Interface](istidevicecontrol-com-interface.md) is needed to get information about the device's ports. The port name used in a call to the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) function can be obtained by calling the **IStiDeviceControl::GetMyDevicePortName** method. For devices on shared ports, such as serial port devices, opening the port in **IStiUSD::Initialize** is not recommended. The port should be opened only in calls to **IStiUSD::LockDevice**. The closing of the ports should be controlled internally to provide fast access. (Opening and closing in **IStiUSD::LockDevice** and **IStiUSD::UnLockDevice** is very inefficient. **CreateFile** can cause a delay making the device appear slow and unresponsive to the user.)

If a WIA driver cannot support multiple [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) calls on the same device port, then the **IStiDeviceControl::GetMyDeviceOpenMode** method should be called.

The WIA driver should check the returned mode value for the STI\_DEVICE\_CREATE\_DATA flag and open the port accordingly.

If the device port must be opened, a call to [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) should be used. When opening a port, the FILE\_FLAG\_OVERLAPPED flag should be used. This allows the OVERLAPPED structure (described in the Windows SDK documentation) to be used when accessing the device. Using overlapped I/O will help control responsive access to the hardware. When a problem is detected, the WIA driver can call **CancelIo** (described in the Windows SDK documentation) to stop all current hardware access.

The following example shows an implementation of the **IStiUSD::Initialize** method.

```cpp
STDMETHODIMP CWIADevice::Initialize(
  PSTIDEVICECONTROL   pIStiDeviceControl,
  DWORD               dwStiVersion,
  HKEY                hParametersKey)
{
  if (!pIStiDeviceControl) {
      return STIERR_INVALID_PARAM;
  }

  HRESULT hr = S_OK;

  //
  // Get the mode of the device to check why we were created.  status, data, or both...
  //

  DWORD dwMode = 0;
  hr = pIStiDeviceControl->GetMyDeviceOpenMode(&dwMode);
  if(FAILED(hr)){
      return hr;
  }

  if(dwMode & STI_DEVICE_CREATE_DATA)
  {
      //
      // device is being opened for data
      //
  }

  if(dwMode & STI_DEVICE_CREATE_STATUS)
  {
      //
      // device is being opened for status
      //
  }

  if(dwMode & STI_DEVICE_CREATE_BOTH)
  {
      //
      // device is being opened for both data and status
      //
  }

  //
  // Get the name of the device port to be used in a call to CreateFile().
  //

  WCHAR szDevicePortNameW[MAX_PATH];
  memset(szDevicePortNameW,0,sizeof(szDevicePortNameW));

  hr = pIStiDeviceControl->GetMyDevicePortName(szDevicePortNameW,
                                            sizeof(szDevicePortNameW)/sizeof(WCHAR));
  if(FAILED(hr)) {
      return hr;
  }

  //
  // Open kernel-mode device driver. Use the FILE_FLAG_OVERLAPPED flag 
  // for proper cancellation
  // of kernel-mode operations and asynchronous file IO. 
  //  The CancelIo() call will function properly if this flag is used.
  //  It is recommended to use this flag.
  //

  m_hDeviceDataHandle = CreateFileW(szDevicePortNameW,
                                   GENERIC_READ | GENERIC_WRITE, // Access mask
                                   0,                            // Share mode
                NULL,                         // SA
                                   OPEN_EXISTING,                // Create disposition
                                   FILE_ATTRIBUTE_SYSTEM|FILE_FLAG_OVERLAPPED,
                                   NULL );

  m_dwLastOperationError = ::GetLastError();

  hr = (m_hDeviceDataHandle != INVALID_HANDLE_VALUE) ?
              S_OK : MAKE_HRESULT(SEVERITY_ERROR,FACILITY_WIN32,m_dwLastOperationError);

  if (FAILED(hr)) {
      return hr;
  }

  //
  // Open DeviceData section to read driver specific information
  //

  HKEY hKey = hParametersKey;
  HKEY hOpenKey = NULL;
  if (RegOpenKeyEx(hKey,                     // handle to open key
                   TEXT("DeviceData"),       // address of name of subkey to open
                   0,                        // options (must be NULL)
                   KEY_QUERY_VALUE|KEY_READ, // just want to QUERY a value
                   &hOpenKey                 // address of handle to open key
     ) == ERROR_SUCCESS) {

      //
      // This is where you read registry entries for your device.
      // The DeviceData section is the proper place to put this 
      // information. Information about your device should
      // have been written using the WIA device's .INF installation
      // file.
      // You can access this information from this location in the
      // Registry. The WIA service owns the hParameters HKEY. 
      // DO NOT CLOSE THIS KEY. Always close any HKEYS opened by
      //  this WIA driver after you are finished.
      //

      //
      // close registry key when finished, reading DeviceData information.
      //

      RegCloseKey(hOpenKey);
  } else {
      return E_FAIL;
  }
  return hr;
}
```

The WIA service calls [**IStiUSD::GetCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff543817) after a successful call to the **IStiUSD::Initialize** method. **IStiUSD::GetCapabilities** then supplies the [**STI\_USD\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff548404) structure with STI version information, WIA support flags (bit flags indicating driver capabilities), and any event requirements.

The following example shows an implementation of **IStiUSD::GetCapabilities**.

```cpp
/********************************************************************\
* CWIADevice::GetCapabilities
* Remarks:
* This WIA driver sets the following capability flags:
* 1. STI_GENCAP_WIA - This driver supports WIA
* 2. STI_USD_GENCAP_NATIVE_PUSHSUPPORT - This driver supports push
*    buttons
* 3. STI_GENCAP_NOTIFICATIONS - This driver requires the use of 
*    interrupt events.
*
\********************************************************************/

STDMETHODIMP CWIADevice::GetCapabilities(PSTI_USD_CAPS pUsdCaps)
{
  //
  // If the caller did not pass in the correct parameters,
  // then fail the call with E_INVALIDARG.
  //

  if (!pUsdCaps) {
      return E_INVALIDARG;
  }

  memset(pUsdCaps, 0, sizeof(STI_USD_CAPS));
  pUsdCaps->dwVersion     = STI_VERSION;    // STI version
  pUsdCaps->dwGenericCaps = STI_GENCAP_WIA| // WIA support
                            STI_USD_GENCAP_NATIVE_PUSHSUPPORT| // button support
                            STI_GENCAP_NOTIFICATIONS; // interrupt event support
  return S_OK;
}
```

 

 




