---
title: Sample Extension Unit Plug-in DLL
description: Sample Extension Unit Plug-in DLL
ms.assetid: bd9ea70d-7bd0-494d-8d67-7a36a41d005b
keywords:
- plug-in DLL WDK USB Video Class
- extension units WDK USB Video Class , samples, plug-in DLL
- sample code WDK USB Video Class , extension unit plug-in DLL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sample Extension Unit Plug-in DLL


This topic contains sample code for an Extension Unit plug-in DLL that exposes a COM API on top of a KS property set.

The sample defines a class called **CExtension**, which derives from **CNodeControl**. The implementation of the **CNodeControl** class is also provided later. **CNodeControl** derives from the Microsoft-supplied **IKsNodeControl** interface, which is defined in *Vidcap.h*.

*Vidcap.ax* uses **IKsNodeControl** to inform the plug-in of the extension node ID and provide it with an instance of **IKsControl**. Specifically, the plug-in receives this information through calls to **CExtension::put\_NodeId** and **CExtension::put\_KsControl**. You can find possible implementations of these methods later in this topic for the parent class **CNodeControl**.

*Vidcap.h* appears in the Summer 2004 DirectX SDK through the February 2005 [DirectX SDK](http://go.microsoft.com/fwlink/p/?linkid=51990). When installing these packages, you must install the Extras to obtain *Vidcap.h*.

In Windows Vista and later releases, *Vidcap.h* is included as part of the Microsoft Windows SDK.

Include the following code in the class header file, arbitrarily named *Xuproxy.h*:

```cpp
#include <ks.h>
#include <ksproxy.h>
#include <C:\Program Files\Microsoft DirectX 9.0 SDK (February 2005)\Extras\DirectShow\Include\vidcap.h>
#include <C:\Program Files\Microsoft DirectX 9.0 SDK (February 2005)\Extras\DirectShow\Include\ksmedia.h>

DEFINE_GUID(CLSID_ExtensionUnit, 0xzzzzzzzz, 0xzzzz, 0xzzzz, 0xzz, 0xzz, 0xzz, 0xzz, 0xzz, 0xzz, 0xzz, 0xzz);

class CNodeControl :
    public IKsNodeControl
{
public:
    STDMETHOD(put_NodeId) (DWORD dwNodeId);
    STDMETHOD(put_KsControl) (PVOID pKsControl);

    DWORD m_dwNodeId;
    CComPtr<IKsControl> m_pKsControl;
};

class CExtension :
   public IExtensionUnit,
   public CComObjectRootEx<CComObjectThreadModel>,
   public CComCoClass<CExtension, &CLSID_ExtensionUnit>,
   public CNodeControl
{
   public:

   CExtension();
   STDMETHOD(FinalConstruct)();

   BEGIN_COM_MAP(CExtension)
      COM_INTERFACE_ENTRY(IKsNodeControl)
      COM_INTERFACE_ENTRY(IExtensionUnit)
   END_COM_MAP()

   DECLARE_PROTECT_FINAL_CONSTRUCT()
   DECLARE_NO_REGISTRY()
   DECLARE_ONLY_AGGREGATABLE(CExtension)

   // IExtensionUnit
   public:
   STDMETHOD (get_Info)(
      ULONG ulSize,
      BYTE pInfo[]);
   STDMETHOD (get_InfoSize)(
      ULONG *pulSize);
   STDMETHOD (get_PropertySize)(
      ULONG PropertyId, 
      ULONG *pulSize);
   STDMETHOD (get_Property)(
      ULONG PropertyId, 
      ULONG ulSize, 
      BYTE pValue[]);
   STDMETHOD (put_Property)(
      ULONG PropertyId, 
      ULONG ulSize, 
      BYTE pValue[]);
   STDMETHOD (get_PropertyRange)(
      ULONG PropertyId, 
      ULONG ulSize,
      BYTE pMin[], 
      BYTE pMax[], 
      BYTE pSteppingDelta[], 
      BYTE pDefault[]);
};

#define STATIC_PROPSETID_VIDCAP_EXTENSION_UNIT \
   0xXXXXXXXX,0xXXXX,0xXXXX,0xXX,0xXX,0xXX,0xXX,0xXX,0xXX,0xXX,0xXX
DEFINE_GUIDSTRUCT("XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX", \ 
   PROPSETID_VIDCAP_EXTENSION_UNIT);
#define PROPSETID_VIDCAP_EXTENSION_UNIT \      
   DEFINE_GUIDNAMED(PROPSETID_VIDCAP_EXTENSION_UNIT)
```

Implement the two virtual methods from **IKsNodeControl** in **CNodeControl**. These methods are then inherited by instances of the **CExtension** class.

The following code is in a source file arbitrarily named *Xuproxy.cpp*:

```cpp
STDMETHODIMP
CNodeControl::put_NodeId(
   DWORD dwNodeId)
{
   m_dwNodeId = dwNodeId;
 return S_OK;
}

STDMETHODIMP
CNodeControl::put_KsControl(
   PVOID pKsControl)
{
   HRESULT hr = S_OK;
   IKsControl *pIKsControl;

 if (!pKsControl) return E_POINTER;
    pIKsControl = (IKsControl *) pKsControl;

    if (m_pKsControl) m_pKsControl.Release();
 hr = pIKsControl->QueryInterface(__uuidof(IKsControl),
       (void **) &m_pKsControl);        

    return hr;
}
```

Also include implementations of **CExtension**'s methods in the same *Xuproxy.cpp* file:

```cpp
CExtension::CExtension()
{
    m_pKsControl = NULL;
}

STDMETHODIMP 
CExtension::FinalConstruct()
{
    if (m_pOuterUnknown == NULL ) return E_FAIL;
    return S_OK;
}

STDMETHODIMP 
CExtension::get_InfoSize(
    ULONG *pulSize)
{
    HRESULT hr = S_OK;
    ULONG ulBytesReturned;
    KSP_NODE ExtensionProp;

    if (!pulSize) return E_POINTER;

    ExtensionProp.Property.Set = PROPSETID_VIDCAP_EXTENSION_UNIT;
    ExtensionProp.Property.Id = KSPROPERTY_EXTENSION_UNIT_INFO;
    ExtensionProp.Property.Flags = KSPROPERTY_TYPE_GET | 
                                   KSPROPERTY_TYPE_TOPOLOGY;
    ExtensionProp.NodeId = m_dwNodeId;

 hr = m_pKsControl->KsProperty(
        (PKSPROPERTY) &ExtensionProp,
        sizeof(ExtensionProp),
        NULL,
        0,
        &ulBytesReturned);

    if (hr == HRESULT_FROM_WIN32(ERROR_MORE_DATA)) 
    {
        *pulSize = ulBytesReturned;
        hr = S_OK;
    }
 
 return hr;
}


STDMETHODIMP 
CExtension::get_Info(
    ULONG ulSize,
    BYTE pInfo[])
{
    HRESULT hr = S_OK;
    KSP_NODE ExtensionProp;
    ULONG ulBytesReturned;

    ExtensionProp.Property.Set = PROPSETID_VIDCAP_EXTENSION_UNIT;
    ExtensionProp.Property.Id = KSPROPERTY_EXTENSION_UNIT_INFO;
    ExtensionProp.Property.Flags = KSPROPERTY_TYPE_GET | 
                                   KSPROPERTY_TYPE_TOPOLOGY;
    ExtensionProp.NodeId = m_dwNodeId;

    hr = m_pKsControl->KsProperty(
        (PKSPROPERTY) &ExtensionProp,
 sizeof(ExtensionProp),
        (PVOID) pInfo,
        ulSize,
        &ulBytesReturned);

 return hr;
}


STDMETHODIMP 
CExtension::get_PropertySize(
    ULONG PropertyId, 
    ULONG *pulSize)
{
    HRESULT hr = S_OK;
    ULONG ulBytesReturned;
    KSP_NODE ExtensionProp;

 if (!pulSize) return E_POINTER;

    ExtensionProp.Property.Set = PROPSETID_VIDCAP_EXTENSION_UNIT;
    ExtensionProp.Property.Id = PropertyId;
    ExtensionProp.Property.Flags = KSPROPERTY_TYPE_GET | 
                                   KSPROPERTY_TYPE_TOPOLOGY;
    ExtensionProp.NodeId = m_dwNodeId;

    hr = m_pKsControl->KsProperty(
        (PKSPROPERTY) &ExtensionProp,
 sizeof(ExtensionProp),
        NULL,
        0,
        &ulBytesReturned);

 if (hr == HRESULT_FROM_WIN32(ERROR_MORE_DATA)) 
    {
        *pulSize = ulBytesReturned;
        hr = S_OK;
    }
 
 return hr;
}

STDMETHODIMP 
CExtension::get_Property(
    ULONG PropertyId, 
    ULONG ulSize, 
    BYTE pValue[])
{
    HRESULT hr = S_OK;
    KSP_NODE ExtensionProp;
    ULONG ulBytesReturned;

    ExtensionProp.Property.Set = PROPSETID_VIDCAP_EXTENSION_UNIT;
    ExtensionProp.Property.Id = PropertyId;
    ExtensionProp.Property.Flags = KSPROPERTY_TYPE_GET | 
                                   KSPROPERTY_TYPE_TOPOLOGY;
    ExtensionProp.NodeId = m_dwNodeId;

    hr = m_pKsControl->KsProperty(
        (PKSPROPERTY) &ExtensionProp,
 sizeof(ExtensionProp),
        (PVOID) pValue,
        ulSize,
        &ulBytesReturned);

    return hr;
}

STDMETHODIMP 
CExtension::put_Property(
    ULONG PropertyId, 
    ULONG ulSize, 
    BYTE pValue[])
{
    HRESULT hr = S_OK;
    KSP_NODE ExtensionProp;
    ULONG ulBytesReturned;

    ExtensionProp.Property.Set = PROPSETID_VIDCAP_EXTENSION_UNIT;
    ExtensionProp.Property.Id = PropertyId;
    ExtensionProp.Property.Flags = KSPROPERTY_TYPE_SET | 
                                   KSPROPERTY_TYPE_TOPOLOGY;
    ExtensionProp.NodeId = m_dwNodeId;

    hr = m_pKsControl->KsProperty(
        (PKSPROPERTY) &ExtensionProp,
 sizeof(ExtensionProp),
        (PVOID) pValue,
        ulSize,
        &ulBytesReturned);

    return hr;
}

STDMETHODIMP
CExtension::get_PropertyRange( 
    ULONG PropertyId,
    ULONG ulSize,
    BYTE pMin[  ],
    BYTE pMax[  ],
    BYTE pSteppingDelta[  ],
    BYTE pDefault[  ])
{
    // IHV may add code here, current stub just returns S_OK
    HRESULT hr = S_OK;
    return hr;
}

CExtension::CExtension()
{
    m_pKsControl = NULL;
}
 
STDMETHODIMP 
CExtension::FinalConstruct()
{
    if (m_pOuterUnknown == NULL) return E_FAIL;
    return S_OK;
}
```

 

 




