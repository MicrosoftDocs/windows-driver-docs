---
title: Supporting Autoupdate Events with Extension Units
description: Supporting Autoupdate Events with Extension Units
ms.assetid: 3dc75f48-adc7-4443-8090-2e61b3306798
keywords:
- autoupdate events WDK USB Video Class
- autoupdate events WDK USB Video Class , extension units
- events WDK USB Video Class
- events WDK USB Video Class , autoupdate with extension units
- extension units WDK USB Video Class , samples
- sample code WDK USB Video Class , autoupdate events
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Autoupdate Events with Extension Units


This topic contains sample code that demonstrates how to support autoupdate events.

Include the following code in the application source, arbitrarily named TestApp.cpp:

```cpp
hEvent = CreateEvent(NULL, FALSE, FALSE, NULL);
if (!hEvent)
{
    printf("CreateEvent failed\n");
    goto errExit;
}
Event.Set = KSEVENTSETID_VIDCAPNotify;
Event.Id = KSEVENT_VIDCAP_AUTO_UPDATE;
Event.Flags = KSEVENT_TYPE_ENABLE;

EventData.NotificationType = KSEVENTF_EVENT_HANDLE;
EventData.EventHandle.Event = hEvent;
EventData.EventHandle.Reserved[0] = 0;
EventData.EventHandle.Reserved[1] = 0;

// register for autoupdate events
hr = m_pKsControl->KsEvent(
    &Event, 
 sizeof(KSEVENT), 
    &EventData, 
 sizeof(KSEVENTDATA), 
    &ulBytesReturned);
if (FAILED(hr))
{
    printf("Failed to register for auto-update event : %x\n", hr);
 goto errExit;
}

// Wait for event for 5 seconds 
dwError = WaitForSingleObject(hEvent, 5000);

// cancel further notifications
hr = m_pKsControl->KsEvent(
    NULL, 
    0, 
    &EventData, 
 sizeof(KSEVENTDATA), 
    &ulBytesReturned);
if (FAILED(hr))  printf("Cancel event returns : %x\n", hr);

if ((dwError == WAIT_FAILED) || 
   (dwError == WAIT_ABANDONED) ||
   (dwError == WAIT_TIMEOUT))
{
    printf("Wait failed : %d\n", dwError);
 goto errExit;
} 
printf("Wait returned : %d\n", dwError);

// handle the autoupdate event..
```

 

 




