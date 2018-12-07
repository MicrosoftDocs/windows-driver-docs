---
title: Defining Callback Objects Example
description: Defining Callback Objects Example
ms.assetid: d987bb95-cbee-46aa-beaf-167572ca4a80
keywords:
- callback objects WDK UMDF , example of defining
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Defining Callback Objects Example


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

The following code example shows how a driver inherits from the [IPnpCallbackHardware](https://msdn.microsoft.com/library/windows/hardware/ff556764) interface to define a device callback object.

```cpp
class CMyDevice :
       // Callback interface exposed to the framework
       public IPnpCallbackHardware 
{// The following data members make up the context
private:
   HANDLE                  m_CompletionPort;
   WINUSB_INTERFACE HANDLE m_UsbHandle;
   UCHAR                   m_BulkOutPipe;
   ULONG                   m_BulkOutMaxPacket;
   ...
// The following methods make up the callback interfaces
public:
    virtual HRESULT stdcall OnPrepareHardware( 
                              IWDFDevice* pDevice
                              );
    STDMETHOD( OnReleaseHardware )( IWDFDevice *pDevice );

   // Method used to create a device callback object
   static HRESULT CreateInstance( 
                     IUnknown **ppUnknown, 
                     IWDFDeviceInitialize *pDeviceInit,
                     HANDLE CompletionPort 
                     );
   ...
};
```

 

 





