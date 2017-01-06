---
Description: Supporting the WPD Infrastructure
MS-HAID: 'wpddk.the\_wpdservicesampledriver\_supporting\_wpd\_infrastructure'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Supporting the WPD Infrastructure
---

# Supporting the WPD Infrastructure


The WPD infrastructure is command driven. When a WPD application calls one of the methods in a given interface, the WPD serializer (an in-process COM server) converts the method call into one or more commands that it sends to the driver. The driver, in turn, processes these commands and then returns a response. For more information about the infrastructure, see the [Architecture Overview](architecture-overview.md) topic.

The following image of the *WpdMon.exe* tool shows the result of an application calling the **IPortableDeviceServiceMethods::Invoke** method to invoke the BeginSync method that is supported by the sample driver:

![the wpd monitor](images/iportabledeviceservicemethods_invoke_method_wpdmon.png)

In the previous image, the WPD serializer converted the **Invoke** call into the WPD\_COMMAND\_SERVICE\_METHODS\_START\_INVOKE command and the corresponding parameters. The driver processed this command and issued two responses to the WPD API. The first response is the result of WPD\_COMMAND\_SERVICE\_METHODS\_START\_INVOKE to indicate that the **StartInvoke**command was successful and that the method started running on the device. The second response is the WPD\_EVENT\_SERVICE\_METHOD\_COMPLETE event that the driver sent when the method completed. The driver sent WPD\_EVENT\_SERVICE\_METHOD\_COMPLETE so that the WPD API could perform the necessary method completion and cleanup. For the sample driver, the two responses followed immediately with no time delay; on an actual device, there can be a delay between the two responses, if a method takes a long time to complete.

The WPD\_COMMAND\_SERVICE\_METHODS\_START\_INVOKE command is first handled in the **WpdService::DispatchWpdMessage** method. This method, in turn, invokes the **WpdServiceMethod::OnStartInvoke** method. The first method is found in the file *WpdService.cpp*; the second is found in the file *WpdServiceMethod.cpp*.

The following excerpt from the **WpdService::DispatchWpdMessage** method in *WpdService.cpp* shows the call to the **WpdServiceMethod::OnStartInvoke** handler. The **DispatchWpdMessage** method passes the command parameters to the handler. These command parameters consist of a pointer to the parameters for the **Invoke** method as well as a pointer to the *pResults* variable that receives the method results:

```
HRESULT WpdService::DispatchWpdMessage(
            REFPROPERTYKEY         Command,
    __in    IPortableDeviceValues* pParams,
    __out   IPortableDeviceValues* pResults)
{
    HRESULT     hr                  = S_OK;
    LPWSTR      pszRequestFilename  = NULL;

    // Get the request filename to process the service message
    hr = pParams->GetStringValue(PRIVATE_SAMPLE_DRIVER_REQUEST_FILENAME, &pszRequestFilename);
    if (FAILED(hr))
    {
        hr = E_INVALIDARG;
        CHECK_HR(hr, "Failed to get the required requested filename");
    }

    if (hr == S_OK)
    {    
        hr = CheckRequestFilename(pszRequestFilename);
        CHECK_HR(hr, "Unknown request filename %ws received", pszRequestFilename);
    }

    if (hr == S_OK)
    {
     …
        else if (IsEqualPropertyKey(Command, WPD_COMMAND_SERVICE_METHODS_START_INVOKE))
        {
            hr = m_ServiceMethods.OnStartInvoke(pParams, pResults);
        }
        …
    return hr;
}
```

## <span id="related_topics"></span>Related topics


****
[The WpdServiceSampleDriverSample](the-wpdservicesampledriver-sample.md)

[The WPD Driver Samples](the-wpd-driver-samples.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Supporting%20the%20WPD%20Infrastructure%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




