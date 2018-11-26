---
title: Asynchronous Notifications in Print Filters
description: Asynchronous Notifications in Print Filters
ms.assetid: 52b0790b-4927-4e1b-8ae5-6e2afc7c9df6
keywords:
- render modules WDK XPSDrv , XPS filters
- XPS filters WDK XPSDrv
- filters WDK XPS
- asynchronous notifications WDK XPS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Asynchronous Notifications in Print Filters


The print filter pipeline has an asynchronous notification feature that is very similar to the asynchronous notification that is supported in the print spooler for applications. The [**RouterCreatePrintAsyncNotificationChannel**](https://msdn.microsoft.com/library/windows/hardware/ff562009) function that is available in the print spooler is not available to print filters. Print filters must use the [IPrintClassObjectFactory](https://msdn.microsoft.com/library/windows/hardware/ff551955) interface to create IPrintAsyncNotify objects.

This topic describes how to use the asynchronous notification feature in a print filter.

**Note**  Throwing asynchronous notifications from a print filter is not supported in the v4 print driver model.

 

### IPrintClassObjectFactory

The [IPrintClassObjectFactory](https://msdn.microsoft.com/library/windows/hardware/ff551955) interface provides access to the notification interfaces. The following code example illustrates how a filter can obtain this interface from the property bag.

```cpp
// This interface is defined as a private member variable in the filter class
IPrintClassObjectFactory  *m_pPrintClassFactory;

// The following code goes in the IntializeFilter method of the filter
VARIANT var;
VariantInit(&var);

HRESULT hr = pIPropertyBag->GetProperty(
    XPS_FP_PRINT_CLASS_FACTORY, 
    &var);

if (SUCCEEDED(hr))
{
    hr = V_UNKNOWN(&var)->QueryInterface(
 IID_IPrintClassObjectFactory,
 reinterpret_cast<void **>(&m_pPrintClassFactory));
}
```

### Notification Channel

With the IPrintClassObjectFactory interface, the filter can create a unidirectional or a bidirectional notification channel, depending on the needs of the filter. The following code example continues from the preceding example and shows how a filter establishes a unidirectional notification channel.

```cpp
// Create a unidirectional notification channel
IPrintAsyncNotifyChannel  *pIAsyncNotifyChannel;
IPrintAsyncNotify  *pIAsyncNotify;

HRESULT hr = m_pPrintClassFactory->GetPrintClassObject(
 m_bstrPrinter,      // The printer name that was read from the property bag
 IID_IPrintAsyncNotify,
 reinterpret_cast<void**>(&pIAsyncNotify)));

if (SUCCEEDED(hr))
{
    hr = pIAsyncNotify->CreatePrintAsyncNotifyChannel(
 m_jobId,
 const_cast<GUID*>(&MS_ASYNCNOTIFY_UI),
 kPerUser,
 kUniDirectional,
        NULL,
        &pIAsyncNotifyChannel));

   // Etc.
}
```

To create a bidirectional notification channel, you would use the following code example in place of the preceding example.

```cpp
// Create a bidirectional notification channel
IPrintAsyncNotifyChannel *pIAsyncNotifyChannel;
IPrintAsyncNotify *pIAsyncNotify;

HRESULT hr = m_pPrintClassFactory->GetPrintClassObject(
 m_bstrPrinterName,   // The printer name that was read from the property bag
 IID_IPrintAsyncNotify,
 reinterpret_cast<void**>(&pIAsyncNotify)));

if (SUCCEEDED(hr))
{
    hr = pIAsyncNotify->CreatePrintAsyncNotifyChannel(
 m_jobId,
 const_cast<GUID*>(& SAMPLE_ASYNCNOTIFY_UI),
 kPerUser,
 kBiDirectional,
 pIAsyncCallback,
        &pIAsyncNotifyChannel));

    // Etc.
}
```

In the preceding code example, variable `pIAsyncCallback` is a pointer to the caller's implementation of the [IPrintAsyncNotifyCallback](http://go.microsoft.com/fwlink/p/?linkid=124755) interface.

In some cases, you must release the bidirectional notification channel when you are done with it. To do this, call the [Release](http://go.microsoft.com/fwlink/p/?linkid=98433) method on [IPrintAsyncNotifyChannel](http://go.microsoft.com/fwlink/p/?linkid=124758). For information about when to release a channel, see [Notification Channel](notification-channel.md).

### Impersonation and Notification

The filter must not impersonate the user account when it calls the IPrintAsyncNotify::CreatePrintAsyncNotifyChannel method. The authorization mechanism in the print spooler requires that it is called from the Local Service account. If the filter must impersonate the account of the user who submitted the job, the filter must revert to itself before it calls CreatePrintAsyncNotifyChannel. After the call returns, the filter can revert back to the user account, if necessary.

**Note**  Even though the notification call is made while in the Local Service context, kPerUser notifications are still sent to the user who submitted the job based on the user association of the job ID.

 

### Adapting the WDK Sample Code

You can adapt the notification sample from the WDK sample code to work in a print filter by replacing the RouterCreatePrintAsyncNotificationChannel call with the following code example.

```cpp
IPrintAsyncNotify  *pIAsyncNotify;

HRESULT hr = m_pPrintClassFactory->GetPrintClassObject(
 m_bstrPrinterName,      // get it from the property bag
 IID_IPrintAsyncNotify,
 reinterpret_cast<void**>(&pIAsyncNotify)));

if (SUCCEEDED(hr))
{
    hr = pIAsyncNotify->CreatePrintAsyncNotifyChannel(
 // the same arguments as for 
 // RouterCreatePrintAsyncNotificationChannel
        );

    // Etc.
}
```

 

 




