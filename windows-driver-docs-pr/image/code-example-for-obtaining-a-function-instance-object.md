---
title: Code Example for Obtaining a Function Instance Object
author: windows-driver-content
description: Code Example for Obtaining a Function Instance Object
MS-HAID:
- 'WIA\_wsd\_scan\_26fd8efa-25af-4aa2-bce4-8ab7b91365cb.xml'
- 'image.code\_example\_for\_obtaining\_a\_function\_instance\_object'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d4e3c5e0-d904-4049-9bc2-6c21d2a6f905
---

# Code Example for Obtaining a Function Instance Object


The following code example contains the declaration of a sample class (CWSDDevice) that contains two class members that are relevant to obtaining the current Function Instance object:

-   CWSDDevice::m\_pFunctionDiscovery

-   CWSDDevice::m\_pFunctionInstance

The code example also shows methods to initialize these members and methods to read device properties from the current Function Instance property store. The **CWSDDevice::InitializeConnection** method illustrates the procedure that is described in [Obtaining a Function Instance Object](obtaining-a-function-instance-object.md) to obtain the current Function Instance object that represents the current web services scanner device instance.

```
/**************************************************************************\
* Sample CWSDDevice class that encapsulates the device communication interface 
\**************************************************************************/

class CWSDDevice
{
public:

    CWSDDevice();

    ~CWSDDevice();

    HRESULT 
    InitializeConnection(
        __in LPCWSTR wszDevicePath);

    HRESULT 
    UnInitializeConnection();

    HRESULT
    OpenPropertyStore(
        __out IPropertyStore **ppPropertyStore);

    HRESULT
    ReadDeviceProperty(
        __in_opt IPropertyStore *pPropertyStore,
        __in const PROPERTYKEY  *pPropertyKey,
        __out BSTR              *pbstrPropertyValue);

private:

    //
    // Flag indicating successful initialization was performed:
    //
    BOOL m_bInitialized;
 
    //
    // Function Discovery object
    //
    IFunctionDiscovery *m_pFunctionDiscovery;

    //
    // Function Instance object (which represents the current device instance)
    //
    IFunctionInstance *m_pFunctionInstance;
};

/**************************************************************************\
* CWSDDevice::InitializeConnection
*
* Initializes the connection to the web services scanner through Function Discovery
*
* Arguments:
*
*    wszDevicePath - unique PNPX ID identifier for the WS scanner, 
*                    returned by IStiDeviceControl::GetMyDevicePortName 
*
* Return Value:
*
*    S_OK if successful, an error HRESULT otherwise
*
\**************************************************************************/

HRESULT InitializeConnection(
    __in LPCWSTR wszDevicePath)
{
    HRESULT                           hr                 = S_OK;
    IFunctionInstanceCollectionQuery *pfiCollectionQuery = NULL;
    IFunctionInstanceCollection      *pfiCollection      = NULL;
    PROPVARIANT                       PropVar            = {0};

    if (m_bInitialized)
    {
        //
        // Initialization was performed once. Treat this is as a
        // re-initialization request: un-initialize and initialize again:
        //
        hr = UnInitialize();
        if (FAILED(hr))
        {
            WIAS_ERROR((g_hInst, "Failed to re-initialize device interface, hr = 0x%08X", hr));
        }
    }

    if (!wszDevicePath)
    {
        hr = E_INVALIDARG;
        WIAS_ERROR((g_hInst, "Failed to initialize device interface, invalid device path argument, hr = 0x%08X", hr));
    }

    if (SUCCEEDED(hr))
    {
        PropVariantInit(&PropVar);
        PropVar.vt = VT_LPWSTR;
        PropVar.pwszVal = (LPWSTR)wszDevicePath;
    }

    if (SUCCEEDED(hr))
    {
        //
        // Create the Function Discovery object
        //
        hr = CoCreateInstance(__uuidof(FunctionDiscovery),
                              NULL,
                              CLSCTX_INPROC_SERVER,
                              __uuidof(IFunctionDiscovery),
                              (void**)&m_pFunctionDiscovery);

        if ((SUCCEEDED(hr)) && (!m_pFunctionDiscovery))
        {
            hr = E_POINTER;
            WIAS_ERROR((g_hInst, "CoCreateInstance(IFunctionDiscovery) returned a NULL m_pFunctionDiscovery, hr = 0x%08X", hr));
        }
        if (FAILED(hr))
        {
            WIAS_ERROR((g_hInst, "CoCreateInstance for IFunctionDiscovery failed, hr = 0x%08X", hr));
        }

    }

    if (SUCCEEDED(hr))
    {
        //
        // Query the Function Discovery object for a collection of
        // Function Instances that are related to this device path
        //
        hr = m_pFunctionDiscovery->CreateInstanceCollectionQuery(FCTN_CATEGORY_PNP,
                                                                 NULL,
                                                                 FALSE,
                                                                 NULL, 
                                                                 &pfiCollectionQuery);
        if ((SUCCEEDED(hr)) && (!pfiCollectionQuery))
        {
            WIAS_ERROR((g_hInst, 
                "IFunctionDiscovery::CreateInstanceCollectionQuery(%ws) returned a NULL IFunctionInstanceCollectionQuery* with hr = 0x%08X", 
                FCTN_CATEGORY_PNP, hr));
            hr = E_POINTER;
        }
        if (FAILED(hr))
        {
            WIAS_ERROR((g_hInst, "IFunctionDiscovery::CreateInstanceCollectionQuery(%ws) failed, hr = 0x%08X", FCTN_CATEGORY_PNP, hr));
        }
    }

    if (SUCCEEDED(hr))
    {
        //
        // Pass in the device path (which contains a PnP-X ID) as a query constraint to the new collection query
        //
        hr = pfiCollectionQuery->AddPropertyConstraint(PKEY_PNPX_ID, &PropVar, QC_EQUALS);

        if (FAILED(hr))
        {
            WIAS_ERROR((g_hInst, "IFunctionInstanceCollectionQuery::AddPropertyConstraint(PKEY_PNPX_ID, %ws) failed, hr = 0x%08X", 
                wszDevicePath, hr));
        }
    }

    if (SUCCEEDED(hr))
    {
        //
        // Execute the query to obtain the unique Function Instance object that identifies our device that is described by wszDevicePath
        //
        hr = pfiCollectionQuery->Execute(&pfiCollection);

        if ((SUCCEEDED(hr)) && (!pfiCollection))
        {
            hr = E_POINTER;
            WIAS_ERROR((g_hInst, 
                "IFunctionInstanceCollectionQuery::Execute returned a NULL IFunctionInstanceCollection* for %ws, hr = 0x%08X",
                wszDevicePath, hr));
        }

        if (FAILED(hr))
        {
            WIAS_ERROR((g_hInst, "IFunctionInstanceCollectionQuery::Execute for DevicePath %ws failed, hr = 0x%08X", 
                wszDevicePath, hr));
        }
    }

    if (SUCCEEDED(hr))
    {
        //
        // Retrieve the unique Function Instance object that identifies our device
        //
        // Note that after the IFunctionDiscovery::CreateInstanceCollectionQuery constraint 
        // the collection must contain a single element, accessible by pfiCollection->Item(0).
        //
        // Without the query constraint, we must search for the Function Instance that corresponds 
        // to our wszDevicePath in the entire collection, using pfiCollection->Count and pfiCollection->Item...
        //
        // See the IFunctionInstanceCollection interface that is defined in FunctionDiscoveryAPI.idl
        //
        //     interface IFunctionInstanceCollection : IUnknown
        //     {
        //         HRESULT GetCount(
        //             [out, retval] DWORD * pdwCount);
        //
        //         HRESULT Item(
        //             [in] DWORD dwIndex,
        //             [out, retval] IFunctionInstance ** ppFunctionInstance);
        //     };
        //
        //

        hr = pfiCollection->Item(0, &m_pFunctionInstance);

        if ((SUCCEEDED(hr)) && (!m_pFunctionInstance))
        {
            WIAS_ERROR((g_hInst, "IFunctionInstanceCollection.Item(0) returned a NULL IFunctionInstance* for %ws with hr = 0x%08X", 
                wszDevicePath, hr));
            hr = E_POINTER;
        }

        if (FAILED(hr))
        {
            WIAS_ERROR((g_hInst, "IFunctionInstanceCollection.Item(0) for %ws failed, hr = 0x%08X", wszDevicePath, hr));
        }
    }

    if (pfiCollection)
    {
        pfiCollection->Release();
        pfiCollection = NULL;
    }

    if (pfiCollectionQuery)
    {
        pfiCollectionQuery->Release();
        pfiCollectionQuery = NULL;
    }

    if (SUCCEEDED(hr))
    {
        WIAS_TRACE((g_hInst, "Device interface successfully initialized", hr));
    }

    if (SUCCEEDED(hr))
    {
        m_bInitialized = TRUE;
    }
    else
    {
        UnInitialize();
    }

    return hr;
}

/**************************************************************************\
* CWSDDevice::UnInitializeConnection
*
* Uninitializes the connection to the web services scanner device
* through Function Discovery.
*
* Arguments:
*
*    none
*
* Return Value:
*
*    S_OK if successful, an error HRESULT otherwise
*
\**************************************************************************/

HRESULT CWSDDevice::UnInitializeConnection()
{
    HRESULT hr = S_OK;

    WIAS_TRACE((g_hInst, "Shutting down the current device connection, if any.."));

    //
    // Release Function Discovery COM interfaces:
    //

    if (m_pFunctionInstance)
    {
        m_pFunctionInstance->Release();
        m_pFunctionInstance = NULL;
    }

    if (m_pFunctionDiscovery)
    {
        m_pFunctionDiscovery->Release();
        m_pFunctionDiscovery = NULL;
    }


    m_bInitialized = FALSE;

    return hr;
}

/**************************************************************************\
* CWSDDevice::CWSDDevice
*
* Constructor for the CWSDDevice class that encapsulates the communication
* interface to the web services-compliant scanner image acquisition device 
*
* Arguments:
*
*   None
*
* Return Value:
*
*   None
*
\**************************************************************************/

CWSDDevice::CWSDDevice()
{
    m_pFunctionDiscovery = NULL;
    m_pFunctionInstance = NULL;

    m_bInitialized = FALSE;

    return;
}

/**************************************************************************\
* CWSDDevice::~CWSDDevice
*
* Destructor for the CWSDDevice class that encapsulates the communication
* interface to the web services-compliant scanner image acquisition device
*
* Arguments:
*
*   None
*
* Return Value:
*
*   None
*
\**************************************************************************/

CWSDDevice::~CWSDDevice()
{
    UnInitializeConnection();
    return;
};
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Code%20Example%20for%20Obtaining%20a%20Function%20Instance%20Object%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


