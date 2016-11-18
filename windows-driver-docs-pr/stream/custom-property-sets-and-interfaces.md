---
title: Custom Property Sets and Interfaces
author: windows-driver-content
description: Custom Property Sets and Interfaces
MS-HAID:
- 'vidcapds\_7d819782-d2fd-4989-bba3-4050deb42908.xml'
- 'stream.custom\_property\_sets\_and\_interfaces'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ea1337e4-c8e5-4971-b602-c066b5a6fd07
keywords: ["interfaces WDK video capture", "custom property sets WDK video capture", "video capture WDK AVStream , property sets", "capturing video WDK AVStream , property sets", "property sets WDK video capture", "custom interfaces WDK video capture"]
---

# Custom Property Sets and Interfaces


Vendors can implement custom property sets to control device-specific or stream-specific parameters. Generally, these kernel property sets are exposed as COM interfaces by a custom *KsProxy* plug-in DLL. Similarly, custom property pages can be implemented to provide user interfaces to control custom property sets.

**To create a custom property set**

1.  Create a unique GUID for your property set by using *Guidgen.exe*. (This tool is included in the Microsoft Windows SDK.)

2.  Implement the property set in your minidriver.

**To create a custom COM interface or property page for your property set**

1.  Create a custom KsProxy plug-in DLL that implements your COM interface or property page. The Class ID (CLSID) for the plug-in DLL must match the property set GUID. Link to *ksproxy.lib* to get the implementation of **::KsSynchronousDeviceControl**.

2.  Add the standard Microsoft DirectShow mechanism of exposing *CFactoryTemplateg\_Templates* from your DLL to allow self-registration of your interface.

3.  Add lines to your hardware's device installation file (INF file) to expose the COM interface and property page as shown in the sample *MyINF.inf* below.

The following code demonstrates an implementation of IAMCameraControl:

**Camera.h**

```
/*
Implements IAMCameraControl via KSPROPERTY_VIDCAP_CAMERACONTROL
*/

class CCameraControlInterfaceHandler :
    public CUnknown,
    public IAMCameraControl {

public:
    DECLARE_IUNKNOWN;

    static CUnknown* CALLBACK CreateInstance(
        LPUNKNOWN UnkOuter,
        HRESULT* hr);

    CCameraControlInterfaceHandler(
        LPUNKNOWN UnkOuter,
        TCHAR* Name,
        HRESULT* hr);

    STDMETHODIMP NonDelegatingQueryInterface(
        REFIID riid,
        PVOID* ppv);
 
    STDMETHODIMP Set( 
            IN long Property,
            IN long lValue,
            IN long Flags);
 
private:
    HANDLE m_ObjectHandle;
};
 
```

**Camera.cpp**

```
/*
Implements IAMCameraControl via KSPROPERTY_VIDCAP_CAMERACONTROL
*/

#include "pch.h"
#include "camera.h"

CUnknown*
CALLBACK
CCameraControlInterfaceHandler::CreateInstance(
    LPUNKNOWN   UnkOuter,
    HRESULT*    hr
    )
{
    CUnknown *Unknown;

    Unknown = new CCameraControlInterfaceHandler(UnkOuter, NAME("IAMCameraControl"), hr);
    if (!Unknown) {
        *hr = E_OUTOFMEMORY;
    }
    return Unknown;
} 

CCameraControlInterfaceHandler::CCameraControlInterfaceHandler(
    LPUNKNOWN   UnkOuter,
    TCHAR*      Name,
    HRESULT*    hr
    ) :
    CUnknown(Name, UnkOuter, hr)
{
    if (SUCCEEDED(*hr)) {
        if (UnkOuter) {
            IKsObject*  Object;
            *hr =  UnkOuter->QueryInterface(uuidof(IKsObject), reinterpret_cast<PVOID*>(&Object));
            if (SUCCEEDED(*hr)) {
                m_ObjectHandle = Object->KsGetObjectHandle();
                // m_Object handle is file handle of the driver
                if (!m_ObjectHandle) {
                    *hr = E_UNEXPECTED;
                }
                Object->Release();
            }
        } else {
            *hr = VFW_E_NEED_OWNER;
        }
    }
}

STDMETHODIMP
CCameraControlInterfaceHandler::Set(
     IN long Property,
     IN long lValue,
     IN long lFlags
     )
{
    KSPROPERTY_CAMERACONTROL_S  CameraControl;
    ULONG       BytesReturned;

 CameraControl.Property.Set = PROPSETID_VIDCAP_CAMERACONTROL;
 CameraControl.Property.Id = Property;
    CameraControl.Property.Flags = KSPROPERTY_TYPE_SET;
    CameraControl.Value = lValue;
 CameraControl.Flags = lFlags;
    CameraControl.Capabilities = 0;

 return ::KsSynchronousDeviceControl(
                m_ObjectHandle,
                IOCTL_KS_PROPERTY,
                &CameraControl,
                sizeof(CameraControl),
                &CameraControl,
                sizeof(CameraControl),
                &BytesReturned);
}

STDMETHODIMP
CCameraControlInterfaceHandler::NonDelegatingQueryInterface(
    REFIID  riid,
    PVOID*  ppv
    )
{
    if (riid == uuidof(IAMCameraControl)) {
        return GetInterface(static_cast<IAMCameraControl*>(this), ppv);
    }
    return CUnknown::NonDelegatingQueryInterface(riid, ppv);
}
```

**MyINF.inf**

```
;IAMCameraControl
HKCR,CLSID\{C6E13370-30AC-11d0-A18C-00A0C9118956},,,%PlugIn_IAMCameraControl%
HKCR,CLSID\{C6E13370-30AC-11d0-A18C-00A0C9118956}\InprocServer32,,,kswdmcap.ax
HKCR,CLSID\{C6E13370-30AC-11d0-A18C-00A0C9118956}\InprocServer32,ThreadingModel,,Both
; This IID is aggregated for the filter given the CLSID of the property set
HKLM,System\CurrentControlSet\Control\MediaInterfaces\{C6E13370-30AC-11d0-A18C-00A0C9118956},,,%PlugIn_IAMCameraControl%
HKLM,System\CurrentControlSet\Control\MediaInterfaces\{C6E13370-30AC-11d0-A18C-00A0C9118956},IID,1,70,33,E1,C6,AC,30,d0,11,A1,8C,00,A0,C9,11,89,56

; CameraControl Property Page
HKCR,CLSID\{71F96465-78F3-11d0-A18C-00A0C9118956},,,%PropPage_CameraControl%
HKCR,CLSID\{71F96465-78F3-11d0-A18C-00A0C9118956}\InprocServer32,,,kswdmcap.ax
HKCR,CLSID\{71F96465-78F3-11d0-A18C-00A0C9118956}\InprocServer32,ThreadingModel,,Both
; Associate the property set with the above property page
HKLM,System\CurrentControlSet\Control\MediaSets\{C6E13370-30AC-11d0-A18C-00A0C9118956}\PropertyPages\{71F96465-78F3-11d0-A18C-00A0C9118956},,,%PropPage_CameraControl%
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Custom%20Property%20Sets%20and%20Interfaces%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


