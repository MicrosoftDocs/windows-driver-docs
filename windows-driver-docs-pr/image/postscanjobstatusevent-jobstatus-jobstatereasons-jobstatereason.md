---
title: PostScanJobStatusEvent.JobStatus.JobStateReasons.JobStateReason
description: PostScanJobStatusEvent.JobStatus.JobStateReasons.JobStateReason
ms.assetid: f10f7f9a-d052-4664-9f14-96699799afbf
keywords: ["PostScanJobStatusEvent.JobStatus.JobStateReasons.JobStateReason"]
---

# PostScanJobStatusEvent.JobStatus.JobStateReasons.JobStateReason


The **JobStateReason** element contains a token that indicates a reason for the status of a post-scan job.

The **JobStateReason** element supports the following values:

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None**  
No additional information is available about the status of the post-scan job.

<span id="NoValidPostScanInstructionsFound"></span><span id="novalidpostscaninstructionsfound"></span><span id="NOVALIDPOSTSCANINSTRUCTIONSFOUND"></span>**NoValidPostScanInstructionsFound**  
The [CreatePostScanJobRequest](createpostscanjobrequest.md) message contained an invalid scan processing instruction.

<span id="CreatePostScanJobFailed"></span><span id="createpostscanjobfailed"></span><span id="CREATEPOSTSCANJOBFAILED"></span>**CreatePostScanJobFailed**  
Failed to create a post-scan job in response to a [CreatePostScanJobRequest](createpostscanjobrequest.md) message.

<span id="SendImageFailed"></span><span id="sendimagefailed"></span><span id="SENDIMAGEFAILED"></span>**SendImageFailed**  
A [SendImageRequest](sendimagerequest.md) message failed to send an image.

<span id="PostScanJobCanceled"></span><span id="postscanjobcanceled"></span><span id="POSTSCANJOBCANCELED"></span>**PostScanJobCanceled**  
A [CancelPostScanJobRequest](cancelpostscanjobrequest.md) message canceled the post-scan job.

<span id="PostScanJobProcessingFailed"></span><span id="postscanjobprocessingfailed"></span><span id="POSTSCANJOBPROCESSINGFAILED"></span>**PostScanJobProcessingFailed**  
The post-scan job failed to run to completion.

<span id="PostScanJobCompletedSuccessfully"></span><span id="postscanjobcompletedsuccessfully"></span><span id="POSTSCANJOBCOMPLETEDSUCCESSFULLY"></span>**PostScanJobCompletedSuccessfully**  
The post-scan job completed successfully.

<span id="PostScanJobCompletedWithErrors"></span><span id="postscanjobcompletedwitherrors"></span><span id="POSTSCANJOBCOMPLETEDWITHERRORS"></span>**PostScanJobCompletedWithErrors**  
The post-scan job completed with errors.

<span id="PostScanJobCompletedWithWarnings"></span><span id="postscanjobcompletedwithwarnings"></span><span id="POSTSCANJOBCOMPLETEDWITHWARNINGS"></span>**PostScanJobCompletedWithWarnings**  
The post-scan job completed with warnings.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20PostScanJobStatusEvent.JobStatus.JobStateReasons.JobStateReason%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




