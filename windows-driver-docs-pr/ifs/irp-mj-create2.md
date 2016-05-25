---
title: IRP\_MJ\_CREATE
author: windows-driver-content
description: IRP\_MJ\_CREATE
ms.assetid: 30684025-9da0-4f4c-a850-ab0390bef091
---

# IRP\_MJ\_CREATE


The following only applies when an existing stream of a file is being opened (that is, newly created streams cannot have pre-existing oplocks on them).

**Note**  When processing IRP\_MJ\_CREATE for any oplock, if the desired access contains nothing other than FILE\_READ\_ATTRIBUTES, FILE\_WRITE\_ATTRIBUTES, or SYNCHRONIZE, the oplock does not break unless FILE\_RESERVE\_OPFILTER is specified. Specifying FILE\_RESERVE\_OPFILTER always results in an oplock break if the create succeeds. For brevity and simplicity, the following table omits the foregoing, since it applies to all oplocks.

 

Request Type
Conditions
Level 1

Broken on IRP\_MJ\_CREATE when:

-   The oplock key associated with the FILE\_OBJECT on which the open is occurring is different from the oplock key associated with the FILE\_OBJECT that owns the oplock.

If the oplock is broken:

-   Break to None **IF**:

    -   The FILE\_RESERVE\_OPFILTER flag is set

        **OR**

    -   Any of the following create disposition values are specified:
        -   FILE\_SUPERSEDE
        -   FILE\_OVERWRITE
        -   FILE\_OVERWRITE\_IF

    **ELSE:**

    -   Break to Level 2.
-   An acknowledgment must be received before the operation continues.

Level 2

Broken on IRP\_MJ\_CREATE when:

-   The oplock key associated with the FILE\_OBJECT on which the open is occurring is different from the oplock key associated with the FILE\_OBJECT that owns the oplock.
-   **AND:**
    -   The FILE\_RESERVE\_OPFILTER flag is set

        **OR**

    -   Any of the following create disposition values are specified:
        -   FILE\_SUPERSEDE
        -   FILE\_OVERWRITE
        -   FILE\_OVERWRITE\_IF

If the oplock is broken:

-   Break to None.

-   No acknowledgment is required, the operation proceeds immediately.

Batch

Broken on IRP\_MJ\_CREATE when:

-   The oplock key associated with the FILE\_OBJECT on which the open is occurring is different from the oplock key associated with the FILE\_OBJECT that owns the oplock.

If the oplock is broken:

-   Break to None **IF**:

    -   The FILE\_RESERVE\_OPFILTER flag is set.

        **OR**

    -   Any of the following create disposition values are specified:
        -   FILE\_SUPERSEDE
        -   FILE\_OVERWRITE
        -   FILE\_OVERWRITE\_IF

    **ELSE:**

    -   Break to Level 2.
-   An acknowledgment must be received before the operation continues.

Filter

Broken on IRP\_MJ\_CREATE when:

-   The oplock key associated with the FILE\_OBJECT on which the open is occurring is different from the oplock key associated with the FILE\_OBJECT that owns the oplock.

-   **AND:**
    -   A "writable" desired access was requested on the stream which was not opened for FILE\_SHARE\_READ access. Note that "writeable" access is defined as any attribute other than:

        -   FILE\_READ\_ATTRIBUTES
        -   FILE\_WRITE\_ATTRIBUTES
        -   FILE\_READ\_DATA
        -   FILE\_READ\_EA
        -   FILE\_EXECUTE
        -   SYNCHRONIZE
        -   READ\_CONTROL

If the oplock is broken:

-   Break to None.

-   An acknowledgment must be received before the operation continues.

Read

Broken on IRP\_MJ\_CREATE when:

-   The oplock key associated with the FILE\_OBJECT on which the open is occurring is different from the oplock key associated with the FILE\_OBJECT that owns the oplock.

-   **AND:**
    -   The FILE\_RESERVE\_OPFILTER flag is set

        **OR**

    -   Any of the following create disposition values are specified:
        -   FILE\_SUPERSEDE
        -   FILE\_OVERWRITE
        -   FILE\_OVERWRITE\_IF

If the oplock is broken:

-   Break to None.

-   No acknowledgment is required, the operation proceeds immediately.

Read-Handle

Broken on IRP\_MJ\_CREATE when:

-   The current open conflicts with an existing open such that a sharing violation would occur.

    **OR**

-   The FILE\_RESERVE\_OPFILTER flag is set.

    **OR**

-   Any of the following create disposition values are specified:

    -   FILE\_SUPERSEDE
    -   FILE\_OVERWRITE
    -   FILE\_OVERWRITE\_IF

    **AND** (for any of the above three conditions)

-   The oplock key associated with the FILE\_OBJECT on which the open is occurring is different from the oplock key associated with the FILE\_OBJECT that owns the oplock.

If the oplock is broken:

-   Break to None **IF**:

    -   The FILE\_RESERVE\_OPFILTER flag is set.

        **OR**

    -   Any of the following create disposition values are specified:
        -   FILE\_SUPERSEDE
        -   FILE\_OVERWRITE
        -   FILE\_OVERWRITE\_IF

    **ELSE:**

    -   Break to Read.
-   If the oplock broke because the current open conflicts with an existing open such that a sharing violation would occur, an acknowledgment must be received before the operation continues.
-   If the oplock broke for any other reason, although acknowledgment of the break is required, the operation continues immediately (for example, without waiting for the acknowledgment).

Read-Write

Broken on IRP\_MJ\_CREATE when:

-   The oplock key associated with the FILE\_OBJECT on which the open is occurring is different from the oplock key associated with the FILE\_OBJECT that owns the oplock.

If the oplock is broken:

-   Break to None **IF**:

    -   The FILE\_RESERVE\_OPFILTER flag is set.

        **OR**

    -   Any of the following create disposition values are specified:
        -   FILE\_SUPERSEDE
        -   FILE\_OVERWRITE
        -   FILE\_OVERWRITE\_IF

    **ELSE:**

    -   Break to Read.
-   An acknowledgment must be received before the operation continues.

Read-Write-Handle

Broken on IRP\_MJ\_CREATE when:

-   The oplock key associated with the FILE\_OBJECT on which the open is occurring is different from the oplock key associated with the FILE\_OBJECT that owns the oplock.

If the oplock is broken:

-   Break to None **IF**:

    -   The FILE\_RESERVE\_OPFILTER flag is set.

        **OR**

    -   Any of the following create disposition values are specified:
        -   FILE\_SUPERSEDE
        -   FILE\_OVERWRITE
        -   FILE\_OVERWRITE\_IF

    **ELSE:**

    -   Break to Read-Write if the current open conflicts with an existing open such that a sharing violation would occur. Otherwise, break to Read-Handle.

-   An acknowledgment must be received before the operation continues.

 

The file system performs additional checks for Batch and Filter oplocks (rather than the oplock package itself) when processing an IRP\_MJ\_CREATE operation, which impact whether the file system asks the oplock package to perform oplock break processing. This is a case where operations on one data stream can impact the oplocks on other data streams of the same file (that is, the last two list items of the following criteria list). If one or more of the following criteria are met, the file system sends a request to the oplock package to perform oplock break processing:

-   Request a break if this is a network query open and a [KTM](http://go.microsoft.com/fwlink/p/?linkid=124745) transaction is present. Otherwise, do not request a break on network query open.

-   If a SUPERSEDE, OVERWRITE or OVERWRITE\_IF operation is performed on an alternate data stream and FILE\_SHARE\_DELETE is not specified and there is a Batch or Filter oplock on the primary data stream, request a break of the Batch or Filter oplock on the primary data stream.

-   If a SUPERSEDE, OVERWRITE or OVERWRITE\_IF operation is performed on the primary data stream and DELETE access has been requested and there are Batch or Filter oplocks on any alternate data stream, request a break of the Batch or Filter oplocks on all alternate data streams that have them.

When the file system decides to ask the oplock package to perform oplock break processing, the rules laid out in the preceding table apply.

The check to break Batch and Filter oplocks occurs before the share access checks are made. This means the Batch or Filter oplock is broken even if the open request ultimately fails due to a sharing violation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20IRP_MJ_CREATE%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


