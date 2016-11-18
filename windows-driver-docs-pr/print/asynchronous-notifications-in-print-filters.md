---
title: Asynchronous Notifications in Print Filters
author: windows-driver-content
description: Asynchronous Notifications in Print Filters
MS-HAID:
- 'xpsfiltpipe\_ca7d1578-a521-4498-941c-73032d7ddb89.xml'
- 'print.asynchronous\_notifications\_in\_print\_filters'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 52b0790b-4927-4e1b-8ae5-6e2afc7c9df6
keywords: ["render modules WDK XPSDrv , XPS filters", "XPS filters WDK XPSDrv", "filters WDK XPS", "asynchronous notifications WDK XPS"]
---

# Asynchronous Notifications in Print Filters


The print filter pipeline has an asynchronous notification feature that is very similar to the asynchronous notification that is supported in the print spooler for applications. The [**RouterCreatePrintAsyncNotificationChannel**](https://msdn.microsoft.com/library/windows/hardware/ff562009) function that is available in the print spooler is not available to print filters. Print filters must use the [IPrintClassObjectFactory](https://msdn.microsoft.com/library/windows/hardware/ff551955) interface to create IPrintAsyncNotify objects.

This topic describes how to use the asynchronous notification feature in a print filter.

**Note**  Throwing asynchronous notifications from a print filter is not supported in the v4 print driver model.

 

### IPrintClassObjectFactory

The [IPrintClassObjectFactory](https://msdn.microsoft.com/library/windows/hardware/ff551955) interface provides access to the notification interfaces. The following code example illustrates how a filter can obtain this interface from the property bag.

```
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

```
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

```
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

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Asynchronous%20Notifications%20in%20Print%20Filters%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


