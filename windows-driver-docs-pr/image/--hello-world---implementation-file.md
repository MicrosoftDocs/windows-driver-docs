---
title: Hello World' Implementation File
description: Hello World' Implementation File
ms.assetid: f81df130-44de-48c5-bfd1-d7e7084e91de
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# 'Hello World' Implementation File

This WIA minidriver is a simple DLL that exports two functions (see ['Hello World' Definition File](--hello-world---definition-file.md)) and implements three COM interfaces (see [Providing a COM Interface](providing-a-com-interface.md)). The following WIA minidriver code example can be compiled into a working driver. The item tree that this WIA minidriver creates has a root item, but no child items, and cannot transfer data.

The *hellowld.cpp* file should contain the following:

```cpp
#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif

#include <stdio.h>
#include <windows.h>
#include <initguid.h>
#include <sti.h>
#include <stiusd.h>
#include <wiamindr.h>

// {7C1E2309-A535-45b1-94B3-9A020EE600C6}
DEFINE_GUID(CLSID_HelloWorldWIADevice, 0x7c1e2309, 0xa535, 0x45b1, 0x94, 0xb3, 0x9a, 0x2, 0xe, 0xe6, 0x0, 0xc6);

#define WIA_DEVICE_ROOT_NAME L"Root" // THIS SHOULD NOT BE LOCALIZED
#define DEFAULT_LOCK_TIMEOUT 1000
class INonDelegatingUnknown {
public:
    virtual STDMETHODIMP NonDelegatingQueryInterface(REFIID riid,LPVOID *ppvObj) = 0;
    virtual STDMETHODIMP_(ULONG) NonDelegatingAddRef() = 0;
    virtual STDMETHODIMP_(ULONG) NonDelegatingRelease() = 0;
};

class CWIADevice : public INonDelegatingUnknown, // NonDelegatingUnknown
          public IStiUSD,               // STI USD interface
          public IWiaMiniDrv            // WIA Minidriver interface
{
public:

//////////////////////////////////////////////////////////////////////
// Constructor/Destructor Section                                 //
//////////////////////////////////////////////////////////////////////

 CWIADevice(LPUNKNOWN punkOuter) : m_cRef(1),
                           m_punkOuter(NULL),
                                   m_pIStiDevice(NULL),
                                   m_pIDrvItemRoot(NULL),
                                   m_lClientsConnected(0) {
   memset(m_WIAFormatInfo,0,sizeof(m_WIAFormatInfo));
     if (punkOuter) {
         m_punkOuter = punkOuter;
     }
 }

 ~CWIADevice() {
     if(m_pIDrvItemRoot) {
         HRESULT hr = m_pIDrvItemRoot->UnlinkItemTree(WiaItemTypeDisconnected);
         m_pIDrvItemRoot->Release();
 m_pIDrvItemRoot = NULL;
     }

     if(m_pIStiDevice) {
         m_pIStiDevice->Release();
         m_pIStiDevice = NULL;
     }
 }

private:
 LONG m_cRef;                      // Device object reference count.
 LONG m_lClientsConnected;         // number of applications connected
 IStiDevice *m_pIStiDevice;        // STI device interface for locking
 IWiaDrvItem *m_pIDrvItemRoot;       // WIA root item
 WIA_FORMAT_INFO m_WIAFormatInfo[2]; // WIA format information
 LPUNKNOWN m_punkOuter;              // Pointer to outer unknown.
public:

//////////////////////////////////////////////////////////////////////
// Standard COM Methods Section                                     //
//////////////////////////////////////////////////////////////////////

 STDMETHODIMP QueryInterface( REFIID riid, LPVOID * ppvObj)
 {
     if (!m_punkOuter) {
         return E_NOINTERFACE;
     }
     return m_punkOuter->QueryInterface(riid,ppvObj);
 }
 STDMETHODIMP_(ULONG) AddRef()
 {
     if (!m_punkOuter) {
         return 0;
     }
     return m_punkOuter->AddRef();
 }
 STDMETHODIMP_(ULONG) Release()
 {
     if (!m_punkOuter) {
         return 0;
     }
     return m_punkOuter->Release();
 }

//////////////////////////////////////////////////////////////////////
// IStiUSD Interface Section (for all WIA drivers)                  //
//////////////////////////////////////////////////////////////////////

 STDMETHOD(Initialize)(THIS_
          PSTIDEVICECONTROL  pHelDcb,
          DWORD              dwStiVersion,
          HKEY               hParametersKey) {return S_OK;}

 STDMETHOD(GetCapabilities)(THIS_ PSTI_USD_CAPS pDevCaps)
 {
     memset(pDevCaps, 0, sizeof(STI_USD_CAPS));
     pDevCaps->dwVersion     = STI_VERSION;    // STI version
     pDevCaps->dwGenericCaps = STI_GENCAP_WIA; // WIA support
     return S_OK;
 }

 STDMETHOD(GetStatus)(THIS_ PSTI_DEVICE_STATUS pDevStatus){return E_NOTIMPL;}
 STDMETHOD(DeviceReset)(THIS){return E_NOTIMPL;}
 STDMETHOD(Diagnostic)(THIS_ LPDIAG pBuffer){return E_NOTIMPL;}
 STDMETHOD(Escape)(THIS_
          STI_RAW_CONTROL_CODE EscapeFunction,
          LPVOID                 lpInData,
          DWORD                  cbInDataSize,
          LPVOID                 pOutData,
          DWORD                  dwOutDataSize,
     LPDWORD                pdwActualData){return E_NOTIMPL;}
 STDMETHOD(GetLastError)(THIS_ LPDWORD pdwLastDeviceError){return E_NOTIMPL;}
 STDMETHOD(LockDevice)(THIS){return S_OK;}
 STDMETHOD(UnLockDevice)(THIS){return S_OK;}
 STDMETHOD(RawReadData)(THIS_
          LPVOID                 lpBuffer,
          LPDWORD                lpdwNumberOfBytes,
          LPOVERLAPPED           lpOverlapped){return E_NOTIMPL;}
 STDMETHOD(RawWriteData)(THIS_
          LPVOID                 lpBuffer,
          DWORD                  nNumberOfBytes,
          LPOVERLAPPED           lpOverlapped){return E_NOTIMPL;}
 STDMETHOD(RawReadCommand)(THIS_
          LPVOID                 lpBuffer,
          LPDWORD                lpdwNumberOfBytes,
          LPOVERLAPPED           lpOverlapped){return E_NOTIMPL;}
 STDMETHOD(RawWriteCommand)(THIS_
          LPVOID                 lpBuffer,
          DWORD                  dwNumberOfBytes,
          LPOVERLAPPED           lpOverlapped){return E_NOTIMPL;}

 STDMETHOD(SetNotificationHandle)(THIS_ HANDLE hEvent){return E_NOTIMPL;}
 STDMETHOD(GetNotificationData)(THIS_ LPSTINOTIFY lpNotify){return E_NOTIMPL;}
 STDMETHOD(GetLastErrorInfo)(THIS_ STI_ERROR_INFO *pLastErrorInfo){return E_NOTIMPL;}

//////////////////////////////////////////////////////////////////////
// IWiaMiniDrv Interface Section (for all WIA drivers)              //
//////////////////////////////////////////////////////////////////////

 STDMETHOD(drvInitializeWia)(THIS_
          BYTE                  *pWiasContext,
          LONG                  lFlags,
          BSTR                  bstrDeviceID,
          BSTR        bstrRootFullItemName,
          IUnknown              *pStiDevice,
          IUnknown              *pIUnknownOuter,
       IWiaDrvItem           **ppIDrvItemRoot,
          IUnknown              **ppIUnknownInner,
          LONG                  *plDevErrVal)
 {
     if ((!pWiasContext)||(!plDevErrVal)) {
         return E_INVALIDARG;
     }

     HRESULT hr = S_OK;

     *plDevErrVal = 0;
     *ppIDrvItemRoot = NULL;
     *ppIUnknownInner = NULL;

     if(!m_pIStiDevice) {
         m_pIStiDevice = reinterpret_cast<IStiDevice*>(pStiDevice);
     }

     if(!m_pIDrvItemRoot) {
         LONG lItemFlags = WiaItemTypeFolder|WiaItemTypeDevice|WiaItemTypeRoot;
         BSTR bstrRootItemName = SysAllocString(WIA_DEVICE_ROOT_NAME);
         if (bstrRootItemName) {
           hr = wiasCreateDrvItem(lItemFlags,  // item flags
                     bstrRootItemName, // item name ("Root")
                 bstrRootFullItemName, // item full name ("0000\Root")
                   (IWiaMiniDrv*)this, // this WIA driver object
                                    0, // size of context
                                 NULL, // context
                &m_pIDrvItemRoot); // created ROOT item
                                       // (IWiaDrvItem interface)
             if (S_OK == hr) {
                 InterlockedIncrement(&m_lClientsConnected);
             }
             SysFreeString(bstrRootItemName);
             bstrRootItemName = NULL;
         } else {
             hr = E_OUTOFMEMORY;
         }
     }
     *ppIDrvItemRoot = m_pIDrvItemRoot;
     return hr;
 }

 STDMETHOD(drvAcquireItemData)(THIS_
           BYTE                      *pWiasContext,
           LONG                      lFlags,
           PMINIDRV_TRANSFER_CONTEXT pmdtc,
           LONG                     *plDevErrVal){return E_NOTIMPL;}
 STDMETHOD(drvInitItemProperties)(THIS_
           BYTE                      *pWiasContext,
           LONG                      lFlags,
           LONG                      *plDevErrVal){return S_OK;}
 STDMETHOD(drvValidateItemProperties)(THIS_
          BYTE                      *pWiasContext,
          LONG                       lFlags,
          ULONG                      nPropSpec,
          const PROPSPEC             *pPropSpec,
          LONG                       *plDevErrVal){return E_NOTIMPL;}
 STDMETHOD(drvWriteItemProperties)(THIS_
           BYTE                      *pWiasContext,
           LONG                      lFlags,
           PMINIDRV_TRANSFER_CONTEXT pmdtc,
           LONG                      *plDevErrVal){return E_NOTIMPL;}
 STDMETHOD(drvReadItemProperties)(THIS_
           BYTE                      *pWiasContext,
           LONG                      lFlags,
           ULONG                     nPropSpec,
           const PROPSPEC            *pPropSpec,
           LONG                      *plDevErrVal){return E_NOTIMPL;}
 STDMETHOD(drvLockWiaDevice)(THIS_
           BYTE                      *pWiasContext,
           LONG                      lFlags,
           LONG                      *plDevErrVal)
    {
     if(m_pIStiDevice)
         return m_pIStiDevice->LockDevice(DEFAULT_LOCK_TIMEOUT);
     else
      return S_OK;
 }

 STDMETHOD(drvUnLockWiaDevice)(THIS_
           BYTE                       *pWiasContext,
           LONG                       lFlags,
           LONG                       *plDevErrVal)
    {
     if(m_pIStiDevice)
         return m_pIStiDevice->UnLockDevice();
     else
         return S_OK;
 }

 STDMETHOD(drvAnalyzeItem)(THIS_
           BYTE                      *pWiasContext,
           LONG                      lFlags,
           LONG                      *plDevErrVal){return E_NOTIMPL;}
 STDMETHOD(drvGetDeviceErrorStr)(THIS_
          LONG                        lFlags,
          LONG                        lDevErrVal,
          LPOLESTR                    *ppszDevErrStr,
          LONG                        *plDevErr){return E_NOTIMPL;}
 STDMETHOD(drvDeviceCommand)(THIS_
          BYTE                        *pWiasContext,
          LONG                        lFlags,
          const GUID                  *plCommand,
          IWiaDrvItem                 **ppWiaDrvItem,
          LONG                        *plDevErrVal){return E_NOTIMPL;}
 STDMETHOD(drvGetCapabilities)(THIS_
          BYTE                         *pWiasContext,
          LONG                         ulFlags,
          LONG                         *pcelt,
          WIA_DEV_CAP_DRV              **ppCapabilities,
          LONG                         *plDevErrVal)
 {
     *pcelt = 0;
     return S_OK;
 }

 STDMETHOD(drvDeleteItem)(THIS_
          BYTE                     *pWiasContext,
          LONG                     lFlags,
          LONG                     *plDevErrVal){return E_NOTIMPL;}
 STDMETHOD(drvFreeDrvItemContext)(THIS_
          LONG                     lFlags,
          BYTE                     *pSpecContext,
          LONG                     *plDevErrVal){return S_OK;}
 STDMETHOD(drvGetWiaFormatInfo)(THIS_
          BYTE                      *pWiasContext,
          LONG                      lFlags,
          LONG                      *pcelt,
          WIA_FORMAT_INFO           **ppwfi,
          LONG                      *plDevErrVal)
 {
     if ((!pWiasContext)||(!plDevErrVal)||(!pcelt)||(!ppwfi)) {
         return E_INVALIDARG;
     }

     if (m_WIAFormatInfo[0].lTymed == TYMED_NULL) {
         m_WIAFormatInfo[0].guidFormatID = WiaImgFmt_MEMORYBMP;
         m_WIAFormatInfo[0].lTymed       = TYMED_CALLBACK;
         m_WIAFormatInfo[1].guidFormatID = WiaImgFmt_BMP;
         m_WIAFormatInfo[1].lTymed       = TYMED_FILE;
     }

     *plDevErrVal = 0;
     *ppwfi = &m_WIAFormatInfo[0];
     *pcelt = 2; // number of formats in returned array
     return S_OK;
 }
 STDMETHOD(drvNotifyPnpEvent)(THIS_
          const GUID                    *pEventGUID,
          BSTR                          bstrDeviceID,
          ULONG                         ulReserved){return E_NOTIMPL;}
 STDMETHOD(drvUnInitializeWia)(THIS_ BYTE *pWiasContext)
 {
     if(InterlockedDecrement(&m_lClientsConnected) < 0) {
         m_lClientsConnected = 0;
     }

     if(m_lClientsConnected == 0) {
         if(m_pIDrvItemRoot) {
             HRESULT hr = m_pIDrvItemRoot->UnlinkItemTree(WiaItemTypeDisconnected);
             m_pIDrvItemRoot->Release();
             m_pIDrvItemRoot = NULL;
         }
     }

     return S_OK;
 }

//////////////////////////////////////////////////////////////////////
// INonDelegating Interface Section (for all WIA drivers)           //
//////////////////////////////////////////////////////////////////////

 STDMETHODIMP NonDelegatingQueryInterface(REFIID  riid,LPVOID  *ppvObj)
 {
     if (!ppvObj) {
         return E_INVALIDARG;
     }

     *ppvObj = NULL;

     if (IsEqualIID( riid, IID_IUnknown )) {
         *ppvObj = static_cast<INonDelegatingUnknown*>(this);
     } else if (IsEqualIID( riid, IID_IStiUSD )) {
         *ppvObj = static_cast<IStiUSD*>(this);
     } else if (IsEqualIID( riid, IID_IWiaMiniDrv )) {
         *ppvObj = static_cast<IWiaMiniDrv*>(this);
     } else {
         return E_NOINTERFACE;
     }

     reinterpret_cast<IUnknown*>(*ppvObj)->AddRef();
     return S_OK;
 }

 STDMETHODIMP_(ULONG) NonDelegatingAddRef()
 {
     return InterlockedIncrement(&m_cRef);
 }

 STDMETHODIMP_(ULONG) NonDelegatingRelease()
 {
     if(InterlockedDecrement(&m_cRef) == 0) {
         delete this;
         return 0;
     }
     return m_cRef;
 }
};

//////////////////////////////////////////////////////////////////////
// IClassFactory Interface Section (for all COM objects)            //
//////////////////////////////////////////////////////////////////////

class CWIADeviceClassFactory : public IClassFactory {
public:
 CWIADeviceClassFactory() : m_cRef(1) {}
 ~CWIADeviceClassFactory(){}
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
     CWIADevice *pDev = new CWIADevice(pUnkOuter);
     if (pDev) {
         hr = pDev->NonDelegatingQueryInterface(riid,ppvObject);
         pDev->NonDelegatingRelease();
     } else {
         hr = E_OUTOFMEMORY;
     }

     return hr;
 }
 STDMETHODIMP LockServer(BOOL fLock){return S_OK;}
private:
 LONG m_cRef;
};

//////////////////////////////////////////////////////////////////////
// DLL Entry Point Section (for all COM objects, in a DLL)          //
//////////////////////////////////////////////////////////////////////

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
 if (IsEqualCLSID(rclsid, CLSID_HelloWorldWIADevice)) {
     CWIADeviceClassFactory *pcf = new CWIADeviceClassFactory;
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

 

 




