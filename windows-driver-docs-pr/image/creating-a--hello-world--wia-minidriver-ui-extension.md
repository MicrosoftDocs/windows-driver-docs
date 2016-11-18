---
title: Creating a "Hello World" WIA Minidriver UI Extension
author: windows-driver-content
description: Creating a \ 0034;Hello World \ 0034; WIA Minidriver UI Extension
MS-HAID:
- 'WIA\_drv\_cus\_5f73e225-8a9f-41c3-b825-d4f30b1a44b0.xml'
- 'image.creating\_a\_\_hello\_world\_\_wia\_minidriver\_ui\_extension'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8de1f8ca-f618-44d7-b6dd-c02cdee8a556
---

# Creating a "Hello World" WIA Minidriver UI Extension


## <a href="" id="ddk-creating-a-hello-world-wia-minidriver-ui-extension-si"></a>


A WIA minidriver UI extension is a simple DLL that exports a few functions and implements at least one of the four following COM interface identifiers (IID):

<a href="" id="iid-iwiauiextension"></a>IID\_IWiaUIExtension  
The interface identifier (IID) for the **IWiaUIExtension** interface. This is the standard WIA interface used to replace the minidriver device icon in My Computer and in Control Panel, and replace the Microsoft common minidriver UI dialogs.

<a href="" id="iid-ishellextinit"></a>IID\_IShellExtInit  
The IID for the **IShellExtInit** interface. This is the standard Windows Shell interface used to initialize Shell extensions for property sheets, shortcut menus, and drag-and-drop handlers (extensions that add items to shortcut menus during nondefault drag-and-drop operations).

<a href="" id="iid-icontextmenu"></a>IID\_IContextMenu  
The IID for the **ContextMenu** interface. This is the standard Windows Shell interface used to create or merge a shortcut menu associated with a Shell object (the WIA minidriver icon in My Computer and in Control Panel).

<a href="" id="iid-ishellpropsheet"></a>IID\_IShellPropSheet  
The IID for the **IShellPropSheet** interface. This is the standard Windows Shell interface used to add or replace pages in the property sheet displayed for a Shell object (the WIA minidriver icon in My Computer and Control Panel).

The "Hello World" WIA minidriver UI extension consists of the following files:

<a href="" id="hellowld-inf"></a>*hellowld.inf*  
This is the installation file (modified to install this UI extension with the original *hellowld* sample).

<a href="" id="hellowldui-def"></a>*hellowldui.def*  
This is the definition file containing the two COM exports, **DllGetClassObject** and **DllCanUnloadNow** (both are described in the Windows SDK documentation).

<a href="" id="hellowldui-cpp"></a>*hellowldui.cpp*  
This is the WIA UI extension implementation.

### Installing WIA UI extensions

To install a WIA UI extension DLL, add **UI Class ID=**{&lt;CLSID of the DLL of your UI extension&gt;} to the INF file under the **DeviceData** section. This CLSID allows clients to call **CoCreateInstance** (described in the Microsoft Windows SDK documentation), and to obtain the supported interfaces of your WIA UI extension.

The following example INF snippet is derived from the WIA minidriver sample in [Creating a 'Hello World' WIA Minidriver](creating-a---hello-world---wia-minidriver.md). The CLSID used by default should be the Microsoft-supplied CLSID for common dialogs, icons, and property pages.

It is recommended that all WIA UI extension DLLs should be self-registering COM objects, to promote easier installation. This sample does not contain a self-registering COM object.

```
[WIADevice.DeviceData]
Server=local
UI DLL=sti.dll
UI Class ID={4DB1AD10-3391-11D2-9A33-00C04FA36145}
```

The following sample is a complete INF file that sets the **UI Class ID** subkey to the CLSID of the *hellowldui* sample UI Extension.

```
; HELLOWLD.INF  -- Hello World WIA Minidriver setup file (with a WIA UI extension DLL)
; Copyright (c) 2002 Hello World Company
; Manufacturer:  Hello World Company

[Version]
Signature="$WINDOWS NT$"
Class=Image
ClassGUID={6bdd1fc6-810f-11d0-bec7-08002be2092f}
Provider=%Mfg%
DriverVer=06/26/2001,1.0
CatalogFile=wia.cat

[DestinationDirs]
DefaultDestDir=11

[Manufacturer]
%Mfg%=Models

[Models]
%WIADevice.DeviceDesc% = WIADevice.Scanner, HELLOWORLD_PNP_ID

[WIADevice.Scanner]
Include=sti.inf
Needs=STI.SerialSection
SubClass=StillImage
DeviceType=1
DeviceSubType=0x0
Capabilities=0x30
DeviceData=WIADevice.DeviceData
AddReg=WIADevice.AddReg
CopyFiles=WIADevice.CopyFiles
ICMProfiles="sRGB Color Space Profile.icm"

[WIADevice.Scanner.Services]
Include=sti.inf
Needs=STI.SerialSection.Services

[WIADevice.DeviceData]
Server=local
UI DLL=sti.dll
UI Class ID={7C1E2309-A535-45b1-94B3-9A020EE600C7}

[WIADevice.AddReg]
HKR,,HardwareConfig,1,1
HKR,,USDClass,,"{7C1E2309-A535-45b1-94B3-9A020EE600C6}"
HKCR,CLSID\{7C1E2309-A535-45b1-94B3-9A020EE600C6},,,"Hello World WIA Minidriver"
HKCR,CLSID\{7C1E2309-A535-45b1-94B3-9A020EE600C6}\InProcServer32,,,%11%\hellowld.dll
HKCR,CLSID\{7C1E2309-A535-45b1-94B3-9A020EE600C6}\InProcServer32,ThreadingModel,,Both

HKCR,CLSID\{7C1E2309-A535-45b1-94B3-9A020EE600C7},,,"Hello World WIA Minidriver UI Extension"
HKCR,CLSID\{7C1E2309-A535-45b1-94B3-9A020EE600C7}\InProcServer32,,,%11%\hellowldui.dll
HKCR,CLSID\{7C1E2309-A535-45b1-94B3-9A020EE600C7}\InProcServer32,ThreadingModel,,Both
HKCR,CLSID\{7C1E2309-A535-45b1-94B3-9A020EE600C7}\shellex\WiaDialogExtensionHandlers\{7C1E2309-A535-45b1-94B3-9A020EE600C7}

[WIADevice.CopyFiles]
hellowld.dll
hellowldui.dll

[SourceDisksFiles.x86]
hellowld.dll=1
hellowldui.dll=1

[SourceDisksNames.x86]
1=%Location%,,,

[SourceDisksFiles.IA64]
hellowld.dll=1
hellowldui.dll=1
[SourceDisksNames.IA64]
1=%Location%,,,

[Strings]
Mfg="Hello World Company"
WIADevice.DeviceDesc="Hello World WIA Minidriver"
Location="Hello World WIA Minidriver Installation Source"
```

The *hellowldui.def* file should contain the following:

```
LIBRARY HELLOWLDUI

EXPORTS
        DllGetClassObject   PRIVATE
        DllCanUnloadNow     PRIVATE
```

The *hellowldui.cpp* file should contain the following:

```
#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif

#include <windows.h>
#include <initguid.h>
#include <wiadevd.h>
#include <shobjidl.h>
#include <shlobj.h>

// {7C1E2309-A535-45b1-94B3-9A020EE600C7}
DEFINE_GUID(CLSID_HelloWorldWIAUIExtension, 0x7c1e2309, 0xa535, 0x45b1, 0x94, 0xb3, 0x9a, 0x2, 0xe, 0xe6, 0x0, 0xc7);

class CWIAUIExtension : public IWiaUIExtension,   // WIA UI Extension interface
                        public IShellExtInit,     // SHELL Extension interface
                        public IContextMenu,      // SHELL context menu Extension interface
                        public IShellPropSheetExt // SHELL property sheet interface
{
public:

    /////////////////////////////////////////////////////////////////////////
    // Construction/Destruction Section                                    //
    /////////////////////////////////////////////////////////////////////////

    CWIAUIExtension() : m_cRef(1) {
    }

    ~CWIAUIExtension() {
    }

private:
    LONG m_cRef; // object reference count.
public:

    /////////////////////////////////////////////////////////////////////////
    // Standard COM Section                                                //
    /////////////////////////////////////////////////////////////////////////

    STDMETHODIMP QueryInterface(REFIID  riid,LPVOID  *ppvObj)
    {
        if (!ppvObj) {
            return E_INVALIDARG;
        }

        *ppvObj = NULL;

        if (IsEqualIID( riid, IID_IUnknown )) {
            *ppvObj = reinterpret_cast<IUnknown*>(this);
        } else if (IsEqualIID( riid, IID_IWiaUIExtension )) {
            *ppvObj = static_cast<IWiaUIExtension*>(this);
        } else {
            return E_NOINTERFACE;
        }

        reinterpret_cast<IUnknown*>(*ppvObj)->AddRef();
        return S_OK;
    }

    STDMETHODIMP_(ULONG) AddRef()
    {
        return InterlockedIncrement(&m_cRef);
    }

    STDMETHODIMP_(ULONG) Release()
    {
        if(InterlockedDecrement(&m_cRef) == 0) {
        delete this;
            return 0;
        }
        return m_cRef;
    }

    /////////////////////////////////////////////////////////////////////////
    // IWiaUIExtension Interface Section                                   //
    /////////////////////////////////////////////////////////////////////////
    STDMETHODIMP DeviceDialog( PDEVICEDIALOGDATA pDeviceDialogData ) {return E_NOTIMPL;}
    STDMETHODIMP GetDeviceIcon( BSTR bstrDeviceId, HICON *phIcon, ULONG nSize ){
 HRESULT hr = E_NOTIMPL;
        HICON hIcon = reinterpret_cast<HICON>(LoadImage(NULL,
                                                        MAKEINTRESOURCE(IDI_APPLICATION),
                                                        IMAGE_ICON,
                                             nSize,
                                                        nSize,
                                                        LR_SHARED));
        if (hIcon) {
            *phIcon = CopyIcon(hIcon);
            hIcon = NULL;
            hr = S_OK;
        }
        return hr;
    }
    STDMETHODIMP GetDeviceBitmapLogo( BSTR bstrDeviceId, HBITMAP *phBitmap, ULONG nMaxWidth, ULONG nMaxHeight ){return E_NOTIMPL;}

    /////////////////////////////////////////////////////////////////////////
    // IShellExtInit Interface Section                                   //
    /////////////////////////////////////////////////////////////////////////
    STDMETHODIMP Initialize (LPCITEMIDLIST pidlFolder,LPDATAOBJECT lpdobj,HKEY hkeyProgID){return E_NOTIMPL;}

    /////////////////////////////////////////////////////////////////////////
    // IContextMenu Interface Section                                   //
    /////////////////////////////////////////////////////////////////////////
    STDMETHODIMP QueryContextMenu (HMENU hmenu,UINT indexMenu,UINT idCmdFirst,UINT idCmdLast,UINT uFlags) {return E_NOTIMPL;}
    STDMETHODIMP InvokeCommand    (LPCMINVOKECOMMANDINFO lpici){return E_NOTIMPL;}
    STDMETHODIMP GetCommandString (UINT_PTR idCmd, UINT uType,UINT* pwReserved,LPSTR pszName,UINT cchMax) {return E_NOTIMPL;}

    /////////////////////////////////////////////////////////////////////////
    // IShellPropSheetExt Interface Section                                   //
    /////////////////////////////////////////////////////////////////////////
    STDMETHODIMP AddPages (LPFNADDPROPSHEETPAGE lpfnAddPage,LPARAM lParam){return E_NOTIMPL;}
    STDMETHODIMP ReplacePage (UINT uPageID,LPFNADDPROPSHEETPAGE lpfnReplacePage,LPARAM lParam) {return E_NOTIMPL;}
};

/////////////////////////////////////////////////////////////////////////
// IClassFactory Interface Section (for all COM objects)               //
/////////////////////////////////////////////////////////////////////////

class CWIAUIClassFactory : public IClassFactory {
public:
    CWIAUIClassFactory() : m_cRef(1) {}
    ~CWIAUIClassFactory(){}
    STDMETHODIMP QueryInterface(REFIID riid, LPVOID *ppv)
    {
      if (!ppv) {
            return E_INVALIDARG;
        }

        *ppv = NULL;
        HRESULT hr = E_NOINTERFACE;
        if (IsEqualIID(riid, IID_IUnknown) || IsEqualIID(riid, IID_IClassFactory)) {
            *ppv = static_cast<IClassFactory*>(this);
            reinterpret_cast<IUnknown*>(*ppv)->AddRef();
            hr = S_OK;
        }
        return hr;
    }
    STDMETHODIMP_(ULONG) AddRef()
    {
        return InterlockedIncrement(&m_cRef);
    }
    STDMETHODIMP_(ULONG) Release()
    {
  if(InterlockedDecrement(&m_cRef) == 0) {
            delete this;
            return 0;
        }
        return m_cRef;
    }
    STDMETHODIMP CreateInstance(IUnknown __RPC_FAR *pUnkOuter,REFIID riid,void __RPC_FAR *__RPC_FAR *ppvObject)
    {
        if ((pUnkOuter)&&(!IsEqualIID(riid,IID_IUnknown))) {
            return CLASS_E_NOAGGREGATION;
        }

        HRESULT hr = E_NOINTERFACE;
        CWIAUIExtension *pUIExt = new CWIAUIExtension();
        if (pUIExt) {
            hr = pUIExt->QueryInterface(riid,ppvObject);
            pUIExt->Release();
        } else {
            hr = E_OUTOFMEMORY;
        }

        return hr;
    }
    STDMETHODIMP LockServer(BOOL fLock){return S_OK;}
private:
    LONG m_cRef;
};

/////////////////////////////////////////////////////////////////////////
// DLL Entry Point Section (for all COM objects, in a DLL)             //
/////////////////////////////////////////////////////////////////////////

extern "C" __declspec(dllexport) BOOL APIENTRY DllEntryPoint(HINSTANCE hinst,DWORD dwReason,LPVOID lpReserved)
{
    switch (dwReason) {
    case DLL_PROCESS_ATTACH:
        break;
    }
    return TRUE;
}

extern "C" STDMETHODIMP DllCanUnloadNow(void){return S_OK;}
extern "C" STDAPI DllGetClassObject(REFCLSID rclsid,REFIID riid,LPVOID *ppv)
{
    if (!ppv) {
        return E_INVALIDARG;
    }
    HRESULT hr = CLASS_E_CLASSNOTAVAILABLE;
    if (IsEqualCLSID(rclsid, CLSID_HelloWorldWIAUIExtension)) {
        CWIAUIClassFactory *pcf = new CWIAUIClassFactory;
        if (pcf) {
            hr = pcf->QueryInterface(riid,ppv);
            pcf->Release();
        } else {
            hr = E_OUTOFMEMORY;
        }
    }
    return hr;
}
```

### Adding a Custom Device Icon

The preceding sample is an example of how to replace the default icon for your device. Replacing the default icon can be an ideal way to guide the user in using the correct device if there is more than one device installed. It will be more intuitive for the user if the icon resembles the attached device.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Creating%20a%20%22Hello%20World%22%20WIA%20Minidriver%20UI%20Extension%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


