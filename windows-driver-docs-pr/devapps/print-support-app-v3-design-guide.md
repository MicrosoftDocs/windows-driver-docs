---
title: Print Support App v3 API Design Guide
description: Provides guidance and examples for printer OEMs and IHVs that are implementing a v3 Print Support App (PSA) for their device.
ms.date: 01/10/2025
ms.topic: concept-article
---

# Print Support Application v3 API design guide

This article provides guidance and examples for printer OEMs and IHVs that are implementing a v3 Print Support App (PSA) for their device.

## Terminology

| Term | Definition |
|--|--|
| PSA | Print Support Application. UWP app that uses the API in this document. |
| IPP | Internet Printing Protocol. Used from a client device to interact with the printer to retrieve and set printing preferences and to send the document to be printed. |
| Print Support Associated Printer | Physical IPP Printer that is linked to PSA. |
| IPP Printer | Printer which supports IPP protocol. |
| PDL | Page description language. The format in which a document is sent to printer. |
| Associated PSA Printer | Physical IPP printer associated with a PSA application. |
| PrintDeviceCapabilities | XML document format for defining printer capabilities. |
| PrintSupportExtension | PSA background task responsible for providing printer constraint extension capabilities. |

## Print support application v3 API

This article contains the v3 extensions to the existing Print Support Application public API described in the Print support app design guide and [**Windows.Graphics.Printing.PrintSupport**](/uwp/api/windows.graphics.printing.printsupport) Namespace. The PSA API enables printer manufacturers to develop Hardware Support apps that can enhance a Windows user's print experience while using inbox Microsoft IPP Class Driver without the need to develop a custom driver. Printing components communicate with the PSA app through a PSA broker process.

For more information, see the following articles:

| Topic | Description |
|--|--|
| [Print Support App design guide](print-support-app-design-guide.md) | Provides guidance and examples for printer OEMs and IHVs that are implementing a print support app (PSA) for their device. |
| [Print Support App v4 API design guide](print-support-app-v4-design-guide.md) | Provides guidance and examples for printer OEMs and IHVs that are implementing a v4 Print Support App (PSA) for their device. |
| [MSIX Manifest Specification for Print Support Virtual Printer](msix-manifest-specification-print-support-virtual-printer.md) | Provides MSIX manifest guidance and examples for printer OEMs and IHVs that are implementing a Print Support Virtual Printer. |
| [Print support app association](print-support-app-association.md) | Provides guidance and examples for associating a print support app (PSA) with a printer. |

The significant extensions to the API are as follows:

- **IPP compression** - PSA v3 API adds a feature to enhance IPP printing by adding an IPP compression feature in a print job for IPP printers that support this feature. Some PSA might have custom compression, which means the IPP job has double compression affecting the performance. To mitigate this, PSA v3 API introduces a property [**IsIppCompressionEnabled**](/uwp/api/windows.graphics.printing.workflow.printworkflowjobstartingeventargs.isippcompressionenabled) and a [**DisableIppCompressionForJob**](/uwp/api/windows.graphics.printing.workflow.printworkflowjobstartingeventargs.disableippcompressionforjob) function (to disable compression for the current job if needed) in the [**PrintWorkflowJobStartingEventArgs**](/uwp/api/windows.graphics.printing.workflow.printworkflowjobstartingeventargs) (PSA v1 API) runtime class.

- **IPP Job Error handling and Error Toast** - PSA v3 API introduces a [**JobIssueDetected**](/uwp/api/windows.graphics.printing.workflow.printworkflowjobbackgroundsession.jobissuedetected) event in [**PrintWorkflowJobBackgroundSession**](/uwp/api/windows.graphics.printing.workflow.printworkflowjobbackgroundsession) (PSA v1 API) runtime class. The event is raised whenever PSA detect an error/warning in the print job. PSA is then responsible for showing the error toast to the user. When PSA registers for this event and sets [**SkipSystemErrorToast**](/uwp/api/windows.graphics.printing.workflow.printworkflowjobissuedetectedeventargs.skipsystemerrortoast) property to true in [**PrintWorkflowJobIssueDetectedEventArgs**](/uwp/api/windows.graphics.printing.workflow.printworkflowjobissuedetectedeventargs), it tells the print system not to show the Windows print system toast. The PSA v3 API also provides a mechanism for PSA to launch the UI when the user interacts with toast.

- **Custom IPP communication timeouts** - PSA v3 API provides an API with which a PSA can override the IPP timeouts. Furthermore, the [**PrintSupportIppCommunicationConfiguration**](/uwp/api/windows.graphics.printing.printsupport.printsupportippcommunicationconfiguration) runtime class is added to [**PrintSupportPrintDeviceCapabilitiesChangedEventArgs**](/uwp/api/windows.graphics.printing.printsupport.printsupportprintdevicecapabilitieschangedeventargs) for manipulating the IPP communication timeouts. In addition, PSA v3 API introduces an event, which is raised when there's an error with the IPP communication. The event was introduced so that IHV could investigate the failure and adjust the timeout values accordingly.

- **Support IPPFaxOut** - PSA v3 API adds a feature to the print system to support IPPFaxOut printers. To support Fax, PSA supports a render filter to convert XPS to Tiff. As PSA might manipulate the XPS content before converting to TIFF, it provides the XpsToTiff enum value in [**PrintWorkflowPdlConversionType**](/uwp/api/windows.graphics.printing.workflow.printworkflowpdlconversiontype) so that PSA can have access to XPS to TIFF converter. In addition, it provides the [**IsIPPFaxOutPrinter**](/uwp/api/windows.devices.printers.ippprintdevice.isIPPFaxOutprinter) property to [**IppPrintDevice**](/uwp/api/windows.devices.printers.ippprintdevice) runtime class so that PSA can differentiate between the standard printer and IPPFaxOut printers.

### Disabling IPP compression

IPP compression is shown in the following code sample.

```csharp
public sealed class PrintSupportWorkflowBackgroundTask : IBackgroundTask
{
    public BackgroundTaskDeferral TaskInstanceDeferral { get; set; }
    private PrintWorkflowJobBackgroundSession session;

    public void Run(IBackgroundTaskInstance taskInstance)
    {
        TaskInstanceDeferral = taskInstance.GetDeferral();

        if (taskInstance.TriggerDetails is PrintWorkflowJobTriggerDetails jobDetails)
        {
            session = jobDetails.PrintWorkflowJobSession;
            session.JobStarting += OnJobStarting;
            session.PdlModificationRequested += OnPdlModificationRequested;
            session.JobIssueDetected += OnJobIssueDetected;

            // Make sure to register all the event handlers before PrintWorkflowJobBackgroundSession.Start is called.
            session.Start();
        }
    }

    private void OnJobStarting(PrintWorkflowJobBackgroundSession sender, PrintWorkflowJobStartingEventArgs args)
    {
        using (args.GetDeferral())
        {
            // Skip system rendering.
            args.SetSkipSystemRendering();

            // If Ipp compression is enabled by the system, check to see if PSA does custom compression for the printer
            // and disable system compression if required.
            if (args.IsIppCompressionEnabled)
            {
                if (this.HasCustomCompression(args.Printer))
                {
                    args.DisableIppCompressionForJob();
                }
            }
        }
    }

    bool HasCustomCompression(IppPrintDevice device)
    {
        bool hasCustomCompression = false;
        // Check if the PSA does custom compression for the printer
        return hasCustomCompression;
    } 
} 
```

### IPP job error handling

This sample demonstrates how the PSA app can register for job errors, show toasts for job errors, and launch the UI when the user activates the toasts.

```csharp
public sealed class PrintSupportWorkflowBackgroundTask : IBackgroundTask
{
    public BackgroundTaskDeferral TaskInstanceDeferral { get; set; }
    private PrintWorkflowJobBackgroundSession session;

    public void Run(IBackgroundTaskInstance taskInstance)
    {
        TaskInstanceDeferral = taskInstance.GetDeferral();

        if (taskInstance.TriggerDetails is PrintWorkflowJobTriggerDetails jobDetails)
        {
            session = jobDetails.PrintWorkflowJobSession;
            session.JobStarting += OnJobStarting;
            session.PdlModificationRequested += OnPdlModificationRequested;
            session.JobIssueDetected += OnJobIssueDetected;

            // Make sure to register all the event handlers before PrintWorkflowJobBackgroundSession.Start is called.
            session.Start();
        }
    }

    private void OnJobIssueDetected (PrintWorkflowJobBackgroundSession sender, PrintWorkflowJobIssueDetectedEventArgs args)
    {
        // Using a deferral to exclude the background process from being suspended while PSA displays UI.
        Deferral deferral = args.GetDeferral();
        var toast = new ToastNotification(GetErrorToastXml(args.ExtendedError,
                args.JobIssueKind, args.PrinterJob, args.Configuration));
        toast.Activated += async (toastSender, e) =>
        {
            // PSA UI application 
            PrintWorkflowUICompletionStatus uiStatus = await args.UILauncher.LaunchAndCompleteUIAsync();
            // Complete deferral
            deferral.Complete();
        };
        toast.Dismissed += async (toastSender, e) => { deferral.Complete(); };
        toast.Failed += async (toastSender, e) => { deferral.Complete(); };
            
        ToastNotificationManager.CreateToastNotifier().Show(toast);
        args.SkipSystemErrorToast = true;
    }

    private XmlDocument GetErrorToastXml(Exception jobError, PrintWorkflowJobIssueKind issueKind,
        PrintWorkflowPrinterJob printerJob, PrintWorkflowConfiguration workflowConfig )
    {
        var errorToastXml = new XmlDocument();
        // Generate Toast XML based on error information from Exception and PrintWorkflowPrinterJob.
        return errorToastXml;
    }
}
```

### Setting IPP communication timeout

This sample demonstrates how to set the IPP communication timeout.

```csharp
public sealed class PrintSupportExtensionBackGroundTask : IBackgroundTask
{
    public BackgroundTaskDeferral TaskInstanceDeferral { get; set; }
    private PrintSupportExtensionSession session;

    public void Run(IBackgroundTaskInstance taskInstance)
    {
        taskInstance.Canceled += OnTaskInstanceCanceled;
        TaskInstanceDeferral = taskInstance.GetDeferral();

        if (taskInstance.TriggerDetails is PrintSupportExtensionTriggerDetails extensionDetails)
        {
            session = extensionDetails.Session;
            session.PrintTicketValidationRequested += OnSessionPrintTicketValidationRequested;
            session.PrintDeviceCapabilitiesChanged += OnSessionPrintDeviceCapabilitiesChanged;
            session.CommunicationErrorDetected += OnCommunicationErrorDetected;

            // Make sure to register all the event handlers before PrintSupportExtensionSession.Start is called.
            session.Start();
        }
    }

    private void OnTaskInstanceCanceled(IBackgroundTaskInstance sender, BackgroundTaskCancellationReason reason)
    {
        session = null;
        TaskInstanceDeferral.Complete();
    }
    
    private void OnSessionPrintDeviceCapabilitiesChanged(PrintSupportExtensionSession sender, PrintSupportPrintDeviceCapabilitiesChangedEventArgs args)
    {
        // Using deferral to exclude the background process from being suspended while PSA updates the printer PDC and other configurations.
        using (args.GetDeferral())
        {
            if (args.CommunicationConfiguration.CanModifyTimeouts)
                {
                    this.UpdateAttributeTimeouts(args.CommunicationConfiguration, sender.Printer);
                    this.UpdateJobTimeouts(args.CommunicationConfiguration, sender.Printer);
                }
                // Do other operations, such as Updating PDC, PDR, and so on here.
        }
    }

    void UpdateAttributeTimeouts(PrintSupportIppCommunicationConfiguration config, IppPrintDevice device)
    {
        IppPrinterCommunicationKind communicationKind = config.CommunicationKind;
        PrintSupportIppCommunicationTimeouts currentTimeouts = config.IppAttributeTimeouts;

        // Adjust attribute timeouts based on the printer
        switch (communicationKind)
        {
            case IppPrinterCommunicationKind.Network:
                currentTimeouts.ConnectTimeout = TimeSpan.FromSeconds(10);
                currentTimeouts.SendTimeout = TimeSpan.FromSeconds(10);
                currentTimeouts.ReceiveTimeout = TimeSpan.FromSeconds(10);
                break;
            case IppPrinterCommunicationKind.UniversalPrint:
                // adjust timeout for universal printer
                break;
        }
        
    }

    void UpdateJobTimeouts(
        PrintSupportIppCommunicationConfiguration config, IppPrintDevice device)
    {
        IppPrinterCommunicationKind communicationKind = config.CommunicationKind;
        PrintSupportIppCommunicationTimeouts currentTimeouts = config.IppJobTimeouts;
        // Adjust job timeouts based on the printer and communication type
        switch (communicationKind)
        {
            case IppPrinterCommunicationKind.Network:
                currentTimeouts.ConnectTimeout = TimeSpan.FromSeconds(30);
                currentTimeouts.SendTimeout = TimeSpan.FromSeconds(30);
                currentTimeouts.ReceiveTimeout = TimeSpan.FromSeconds(30);
                break;
            case IppPrinterCommunicationKind.UniversalPrint:
                // adjust timeout for universal printer
                break;
        }
    }
}
```

### Handling IPP communication errors

This sample demonstrates how to handle IPP communication errors.

```csharp
public sealed class PrintSupportExtensionBackGroundTask : IBackgroundTask
{
    public BackgroundTaskDeferral TaskInstanceDeferral { get; set; }
    private PrintSupportExtensionSession session;
    public void Run(IBackgroundTaskInstance taskInstance)
    {
        taskInstance.Canceled += OnTaskInstanceCanceled;
        TaskInstanceDeferral = taskInstance.GetDeferral();

        if (taskInstance.TriggerDetails is PrintSupportExtensionTriggerDetails extensionDetails)
        {
            session = extensionDetails.Session;
            session.PrintTicketValidationRequested += OnSessionPrintTicketValidationRequested;
            session.PrintDeviceCapabilitiesChanged += OnSessionPrintDeviceCapabilitiesChanged;
            session.CommunicationErrorDetected += OnCommunicationErrorDetected ;

            // Make sure to register all the event handlers before PrintSupportExtensionSession.Start is called.
            session.Start();
        }
    }

    private void OnTaskInstanceCanceled(IBackgroundTaskInstance sender, BackgroundTaskCancellationReason reason)
    {
        session = null;
        TaskInstanceDeferral.Complete();
    }

    private void OnCommunicationErrorDetected(PrintSupportExtensionSession sender, PrintSupportCommunicationErrorDetectedEventArgs args)
    {
        // Using deferral to exclude the background process from being suspended while PSA updates the timeouts.
        using (args.GetDeferral())
        {

            if (args.ErrorKind == IppCommunicationErrorKind.Timeout)
            {
                PrintSupportIppCommunicationConfiguration ippConfig = args.CommunicationConfiguration;
                IppPrintDevice device = sender.Printer;
                // Update timeout based on the communication error
            }
        }
    }  
}
```

### Printing to IPP fax out printer in PSA

This sample demonstrates how to print to an IPPFaxOut printer in a PSA.

```csharp
public sealed class PrintSupportWorkflowBackgroundTask : IBackgroundTask
{
    public BackgroundTaskDeferral TaskInstanceDeferral { get; set; }
    private PrintWorkflowJobBackgroundSession session;

    public void Run(IBackgroundTaskInstance taskInstance)
    {
        TaskInstanceDeferral = taskInstance.GetDeferral();

        if (taskInstance.TriggerDetails is PrintWorkflowJobTriggerDetails jobDetails)
        {
            session = jobDetails.PrintWorkflowJobSession;
            session.JobStarting += OnJobStarting;
            session.PdlModificationRequested += OnPdlModificationRequested;
            session.JobIssueDetected += OnJobIssueDetected;

            // Make sure to register all the event handlers before PrintWorkflowJobBackgroundSession.Start is called.
            session.Start();
        }
    }

    private async void OnPdlModificationRequested(PrintWorkflowJobBackgroundSession sender, PrintWorkflowPdlModificationRequestedEventArgs args)
    {
        using (args.GetDeferral())
        {
            IppPrintDevice printer = args.PrinterJob.Printer;
            IInputStream xpsContent = args.SourceContent.GetInputStream();
            WorkflowPrintTicket printTicket = args.PrinterJob.GetJobPrintTicket();

            string documentFormat = this.GetPrinterDocumentFormat(printer);
            PrintWorkflowPdlTargetStream targetStream = args.CreateJobOnPrinter(documentFormat);
            IInputStream xpsSourceContent = xpsContent;
            if (printer.IsIPPFaxOutPrinter)
            {                    
                // Add cover page to XPS source document   
                xpsSourceContent = this.AddCoverPageToXpsContent(xpsContent);
            }
            
            PrintWorkflowPdlConverter pdlConverter;
            switch (documentFormat.ToLowerInvariant())
            {
                case "image/pwg-raster":
                    pdlConverter = args.GetPdlConverter(PrintWorkflowPdlConversionType.XpsToPwgr);
                    break;
                case "application/pclm":
                    pdlConverter = args.GetPdlConverter(PrintWorkflowPdlConversionType.XpsToPclm);
                    break;
                case "application/pdf":
                    pdlConverter = args.GetPdlConverter(PrintWorkflowPdlConversionType.XpsToPdf);
                    break;
                case "image/tiff":
                    pdlConverter = args.GetPdlConverter(PrintWorkflowPdlConversionType.XpsToTiff);
                    break;
                default:
                    // This should not happen, aborting workflow if PSA does not identify the supported PDLs
                    args.Configuration.AbortPrintFlow(PrintWorkflowJobAbortReason.JobFailed);
                    return;
                }
                // Use pdlConverter to convert the source XPS stream to printer's document format and send it to the printer using targetStream.
                await pdlConverter.ConvertPdlAsync(printTicket, xpsSourceContent, targetStream.GetOutputStream());

                targetStream.CompleteStreamSubmission(PrintWorkflowSubmittedStatus.Succeeded);
            }
        }

    private IInputStream AddCoverPageToXpsContent(IInputStream xpsStream)
    {
        var coverPageXps = new InMemoryRandomAccessStream();
        // Add cover page to XPS content and write to coverPageXps stream
        return coverPageXps;
    }
}
```

### Disabling Fax UI for phone number from PSA

With the IPP fax printer's support, this sample shows a UI for requesting the user to enter the Fax number when printing to the Fax printer. But the PSA might want to show its own UI with more information and options. Since it's confusing for the user if there are two UIs for fax, this sample illustrates an option for a PSA to disable the system UI when they want to show their Fax UI.

The following sample demonstrates the API usage.

```csharp
public sealed class PrintSupportWorkflowBackgroundTask : IBackgroundTask
{

    private void OnJobStarting(PrintWorkflowJobBackgroundSession sender, PrintWorkflowJobStartingEventArgs args)
    {
        using (args.GetDeferral())
        {
            // If the job is printing to an Ipp fax printer,
            // check whether PSA has a custom UI and disable system UI for getting the fax number.
            if (args.IsIPPFaxOutPrinter)
            {
                if (this.HasCustomUIForFax(args.Printer))
                {
                    args.SkipSystemFaxUI = true;
                }
            }
        }
    }

    bool HasCustomUIForFax(IppPrintDevice device)
    {
        bool hasCustomUIForFax = false;
        // Check if the PSA does custom UI for the given fax printer.
        return hasCustomUIForFax;
    }  
}
```

## Remarks

Samples in this article are built on top of the samples of the PSA v1 and v2 APIs in the [Print support app design guide](print-support-app-design-guide.md) with the assumption that the developer is familiar with PSA API workflow.

This article contains the extensions for the existing public Print Support Application API described in Print Support App design guide and [**Windows.Graphics.Printing.PrintSupport**](/uwp/api/windows.graphics.printing.printsupport) Namespace. The PSA API enables printer manufacturers to develop UWP apps that can enhance a Windows users print experience while using inbox Microsoft IPP Class Driver, without the need of developing a custom driver.

Printing components are communicating to the PSA app through a PSA broker process.

## Related articles

[**DisableIppCompressionForJob**](/uwp/api/windows.graphics.printing.workflow.printworkflowjobstartingeventargs.disableippcompressionforjob)

[End of servicing plan for third-party printer drivers on Windows](../print/end-of-servicing-plan-for-third-party-printer-drivers-on-windows.md)

[**IsIppCompressionEnabled**](/uwp/api/windows.graphics.printing.workflow.printworkflowjobstartingeventargs.isippcompressionenabled)

[**IsIPPFaxOutPrinter**](/uwp/api/windows.devices.printers.ippprintdevice.isIPPFaxOutprinter)

[**IppPrintDevice**](/uwp/api/windows.devices.printers.ippprintdevice)

[**JobIssueDetected**](/uwp/api/windows.graphics.printing.workflow.printworkflowjobbackgroundsession.jobissuedetected)

[**PrintSupportIppCommunicationConfiguration**](/uwp/api/windows.graphics.printing.printsupport.printsupportippcommunicationconfiguration)

[**PrintSupportPrintDeviceCapabilitiesChangedEventArgs**](/uwp/api/windows.graphics.printing.printsupport.printsupportprintdevicecapabilitieschangedeventargs)

[**PrintWorkflowJobBackgroundSession**](/uwp/api/windows.graphics.printing.workflow.printworkflowjobbackgroundsession)

[**PrintWorkflowJobIssueDetectedEventArgs**](/uwp/api/windows.graphics.printing.workflow.printworkflowjobissuedetectedeventargs)

[**PrintWorkflowJobStartingEventArgs**](/uwp/api/windows.graphics.printing.workflow.printworkflowjobstartingeventargs)

[**PrintWorkflowPdlConversionType**](/uwp/api/windows.graphics.printing.workflow.printworkflowpdlconversiontype)

[**SkipSystemErrorToast**](/uwp/api/windows.graphics.printing.workflow.printworkflowjobissuedetectedeventargs.skipsystemerrortoast)

[**Windows.Graphics.Printing.PrintSupport**](/uwp/api/windows.graphics.printing.printsupport)
