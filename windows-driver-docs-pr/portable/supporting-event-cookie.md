---
Description: Supporting Event Cookies
title: Supporting Event Cookies
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Event Cookies


WPD applications can specify a unique string or "cookie" in the client information when they call either the **IPortableDevice::Open** method or the **IPortableDeviceService::Open** method. When these applications register their event handlers with a driver, the driver returns this cookie with the event data. By examining the cookie, an application can determine whether it should handle the given event.

For example, Application A creates an object on the device and receives a WPD\_EVENT\_OBJECT\_ADDED event that contains its client event cookie. Application A can choose not to refresh its view of the device contents because the view was updated at the time the object was created. If Application B creates another object on the device, Application A receives a WPD\_EVENT\_OBJECT\_ADDED event that has a different cookie (or no cookie). By examining the cookie, Application A can take the appropriate action and refresh the device contents view, because Application B added the new object. Because WPD events are broadcast to all applications, event cookies are most useful when an application filters out events that it had triggered during a previous interaction with the device.

Depending on the application, the cookie might contain the executable name for the application or the CLSID, or a unique identifier that the application creates if it can run multiple instances at the same time. The actual string contents do not matter to the driver.

In an environment where there can be two or more client applications communicating with your driver (Windows Explorer is virtually guaranteed to be one client through the WPD Shell Namespace Extension), it is a good idea to support the event cookie mechanism. Doing so is a good WPD programming practice that can help reduce the client traffic to your device in response to events and streamline application-side event handling.

## <span id="Steps_to_Support_the_Event_Cookie"></span><span id="steps_to_support_the_event_cookie"></span><span id="STEPS_TO_SUPPORT_THE_EVENT_COOKIE"></span>Steps to Support the Event Cookie


The following steps identify how you can support the WPD\_CLIENT\_EVENT\_COOKIE in a WPD driver:

1.  Add a handler for the WPD\_COMMAND\_COMMON\_SAVE\_CLIENT\_INFORMATION command. The WpdWudfSampleDriver from the WDK contains an example of this in the **WpdBaseDriver::OnSaveClientInfo** method.
2.  In the **OnSaveClientInfo** method, if the application sets WPD\_CLIENT\_EVENT\_COOKIE in the client information parameters, save the cookie with your context info. Some applications might choose not to send this cookie, in which case your driver does not have to do anything for this step.
3.  When you post events, if the client event cookie is available, send it along with the event parameters. In the sample driver, this code will be added to the **PostWpdEvent** function.

The following code example shows how the WpdWudfSampleDriver handles step two in the previous list.

```ManagedCPlusPlus
LPWSTR pszEventCookie = NULL; 
hr = pClientInfo->GetStringValue(WPD_CLIENT_EVENT_COOKIE, &pszEventCookie);
if (hr == S_OK && pszEventCookie != NULL){    
// Store the cookie value with the client context    
pContext->EventCookie = pszEventCookie;
}
CoTaskMemFree(pszEventCookie);
```

The following code example shows how the WpdWudfSampleDriver handles step three in the previous list.

```ManagedCPlusPlus
HRESULT hrEventCookie = GetClientEventCookie(pCommandParams, &pszEventCookie);
if (hrEventCookie == S_OK && pszEventCookie != NULL)
{    
// Add it to the event parameters    
// The application&#39;s OnEvent callback will match this with its cookie    
hrEventCookie = pEventParams->SetStringValue(WPD_CLIENT_EVENT_COOKIE, pszEventCookie);
}
CoTaskMemFree(pszEventCookie);
```

The following code example contains an outline of the GetClientEventCookie helper function. The helper function uses the client information context that is supplied in the command parameters to look up the saved client cookie in the context map.

```ManagedCPlusPlus
ClientContext* pClientContext = NULL;   
// This is a context helper object defined by the sample 
driverhr = pCommandParams->GetStringValue(WPD_PROPERTY_COMMON_CLIENT_INFORMATION_CONTEXT, &pszClientContext);
if (hr == S_OK)
{    
hr = GetClientContext(pCommandParams, pszClientContext, (IUnknown**)&pClientContext);    
if (hr == S_OK && pClientContext != NULL && pClientContext->EventCookie.GetLength() > 0)    
{       
// Allocate the cookie string to return        
*ppszEventCookie = AtlAllocTaskWideString(pClientContext->EventCookie);    
}    
if (pClientContext != NULL)          
pClientContext->Release();    
CoTaskMemFree(pszClientContext);
}
```

 

 




