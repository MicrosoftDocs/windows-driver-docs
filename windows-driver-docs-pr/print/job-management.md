---
title: Job Management
description: A job management feature has been introduced in Windows 8.1 and later versions of Windows to provide a live view of the job queue.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Job Management


A job management feature has been introduced in Windows 8.1 and later versions of Windows to provide a live view of the job queue.

This feature also allows a client to cancel a print job. A client can call the appropriate programming interface from within a UWP device app or from a printer extension.

## The new interfaces


The following interfaces have been introduced in Windows 8.1 to implement the job management feature.

[**IPrinterQueue2**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterqueue2)

[**IPrinterQueueView**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterqueueview)

[**IPrinterQueueViewEvent**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterqueueviewevent)

[**IPrintJob**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintjob)

[**IPrintJobCollection**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintjobcollection)

## Initiating a job management session


To initiate a job management session you must first specify and request a range of jobs that you want to manage. This range of jobs is called a “view,” and you use the [**IPrinterQueue2::GetPrinterQueueView**](/windows-hardware/drivers/ddi/printerextension/nf-printerextension-iprinterqueue2-getprinterqueueview) method to specify it.

If you want to change the view to monitor a different set of jobs, you can use the [**IPrinterQueueView::SetViewRange**](/windows-hardware/drivers/ddi/printerextension/nf-printerextension-iprinterqueueview-setviewrange) method to do that.

Note that the print queue is a dynamic queue. So each time the status of the print queue changes, an event is fired off and the [**IPrinterQueueViewEvent::OnChanged**](/windows-hardware/drivers/ddi/printerextension/nf-printerextension-iprinterqueueviewevent-onchanged) method provides an updated snapshot of the view that was requested.

The following C# code snippet illustrates the use of the new interfaces for initiating a job management session.

```csharp
void PerformJobManagement(IPrinterQueue2 queue)
{
    //
    // Create a printer queue view and specify the range of
    // print queue positions to be monitored
    //

    PrinterQueueView queueView = queue.GetPrinterQueueView(0, COUNT_JOBS_MONITORED);

    //
    // Add the event handler to the IPrinterQueueView object via the 
    // standard COM event model, the IConnectionPoint mechanism.
    //

    queueView.OnChanged += queueView_OnChanged;


    //
    // When a different range of print jobs needs to be monitored, 
    // reset/update the view.
    //

    queueView.SetViewRange(20, COUNT_JOBS_MONITORED);

}

//
// Create an event handler that is called when
// there is a change in the View
//
void queueView_OnChanged(
    IPrintJobCollection pcollection,
    uint ulviewOffset,
    uint ulviewSize,
    uint ulcountJobsInPrintQueue)
{
    foreach (IPrintJob job in pCollection)
    {
        UIDisplay(job.Name);
        UIDisplay(job.Id);
    }
}
```

UIDisplay is used a generic name for the mechanism that you develop for displaying the information to the user.

And also, note that job enumeration starts when the first event handler is added and it is stopped when the last event handler is removed.

## Related topics
[**IPrinterQueue2**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterqueue2)  
[**IPrinterQueueView**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterqueueview)  
[**IPrinterQueueViewEvent**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterqueueviewevent)  
[**IPrintJob**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintjob)  
[**IPrintJobCollection**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintjobcollection)
