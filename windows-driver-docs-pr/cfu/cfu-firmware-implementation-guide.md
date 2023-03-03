---
title: Component Firmware Update (CFU) firmware implementation guide
description: Provides detailed guidance on implementing the Component Firmware Update (CFU) protocol and creating new firmware images to install on the target device.
ms.date: 03/03/2023
---

# Component Firmware Update (CFU) firmware implementation guide

Component Firmware Update (CFU) is a protocol and a process for submitting new firmware images to be installed on the target device.

> [!NOTE]
> CFU is available in Windows 10, version 2004 (Windows 10 May 2020 Update) and later versions.

CFU submissions to the resident firmware are file pairs, one file is the offer part, the other file is the content part. Each CFU submission (each offer and content pair) is required to be created off-line before the submission is sent to the firmware that implements the CFU process.

In the sample [Firmware](https://github.com/Microsoft/CFU/tree/master/Firmware) source code in the CFU repository on GitHub, the general implementation agnostic common code for CFU is contained in `ComponentFwUpdate.c`. All other files are helper files that can be updated or modified to the developer's unique implementation.

## Contents

- [The offer and content parts](#the-offer-and-content-parts)
  - [Offer register details](#offer-register-details)
  - [Processing offers](#processing-offers)
    - [Interpreting the offer](#interpreting-the-offer)
      - [Step 1 - Check bank](#step-1---check-bank)
      - [Step 2 - Check hwVariantMask](#step-2---check-hwvariantmask)
      - [Step 3 - Check firmware version](#step-3---check-firmware-version)
      - [Step 4 - Accept offer](#step-4---accept-offer)
  - [Process the content](#process-the-content)
    - [The structure of the content command](#the-structure-of-the-content-command)
    - [The first block](#the-first-block)
    - [Any other block except first or last](#any-other-block-except-first-or-last)
    - [The last block](#the-last-block)
    - [Clean up after last block](#clean-up-after-last-block)
  - [Forced reset checked](#forced-reset-checked)

## The offer and content parts

The offer and content make up a pair of files in the CFU schema.

The offer part is simply a 16-byte long file that maps to the FWUPDATE_OFFER_COMMAND structure outlined below.  

The content part, the actual firmware to be updated is in the format dictated by the end-user developer.  The provided CFU sample code uses SREC files for firmware content.

The offer is a 16-byte sequence.  This offer structure is put into the offer file.  It's essentially binary data, not text, because the offer contains bit fields of specific meaning.

The offer that is represented in the file maps to this C structure:

```cpp
typedef struct
{
   struct
   {
       UINT8 segmentNumber;
       UINT8 reserved0 : 6;
       UINT8 forceImmediateReset : 1;
       UINT8 forceIgnoreVersion : 1;
       UINT8 componentId;
       UINT8 token;
   } componentInfo;

   UINT32 version;
   UINT32 hwVariantMask;
   struct
   {
       UINT8 protocolRevision : 4;
       UINT8 bank : 2;
       UINT8 reserved0 : 2;
       UINT8 milestone : 3;
       UINT8 reserved1 : 5;
       UINT16 productId;
   } productInfo;

} FWUPDATE_OFFER_COMMAND;
```

From low address to high address, the first byte of the offer is a segment number.

```text
  <------- 4 bytes -----------> <-- 8 bytes -->  <-------- 4 bytes --------->
+================================-=============================================+
|  15:0 7:3  2:0  7:6  5:4  3:0   31:0   31:0     7:0  7:0  7:7  6:6  5:0  7:0 |
|  PI | R1 | MS | R0 | BK | PR  | VM   | VN   |   TK | CI | FV | FR | R0 | SN  |
+================================-=============================================+
```

From high address to low address:

```text
Byte(s)    Value
---------------------------------------------------------
15:14   |  (PI)  Product ID is 2 bytes
13      |  (R1)  Reserved1 5-bit register
        |  (MS)  Milestone 3-bit register
12      |  (R2)  Reserved2 2-bit register
        |  (BK)  Bank 2-bit register
        |  (PR)  Protocol Revision  2-bit register
11:8    |  (VM)  Hardware Variant Mask 32-bit register
7:4     |  (VN)  Version 32-bit register
3       |  (TK)  Token byte 8-bit register
2       |  (CI)  Component ID 8-bit register
1       |  (FV)  Force version bit  1-bit register
        |  (FR)  Force Immediate Reset  1-bit register
        |  (R0)  Reserved0 6-bit register
0       |  (SN)  Segment Number 8-bit register
---------------------------------------------------------
```

### Offer register details

The Product ID. A unique product ID value for this CFU image can be applied to this field.

```cpp
UINT16 productID;  
```

The milestone of the firmware the offer's content represents. Milestones could be different versions of the HW build, for example, EV1 build, EV2 build, and so on. Milestone definition and value assignment are left to the developer.

```cpp
UINT8 milestone : 3;
```

If the firmware is intended for a specific bank - the 2-bit field supports four banks.   The use of a bank register is included in the format of the offer because there are instances where the target devices use banked firmware regions.

If that were the case, and the offer was meant to update a bank in use, the firmware that implements CFU on the target can reject the offer.  Else, the firmware on the target implementing CFU can take other action as warranted.

If banking of firmware images is NOT in the design of the end-user firmware, then it's reasonable to ignore this field (set to whatever values that are convenient, but the value in the bank field is optional and depends on the way in which the on target firmware implements CFU).

```cpp
UINT8 bank : 2;
```

The protocol version of the CFU protocol used is in 4 bits.

```cpp
UINT8 protocolRevision : 4;
```

The bitmask corresponding to all unique HW this firmware image can operate on. For example, the offer may signify it can run on verX of HW but not on verY of HW. Bit definition and value assignment are left to the developer.

```cpp
UINT32 hwVariantMask;
```

The version of the firmware being offered.

```cpp
UINT32 version;
```

A byte token to identify the user specific software making the offer. This is intended to differentiate between drivers and tools that may both be trying to update the same running firmware. For example, a CFU update driver may be assigned token 0xA and a development updater tool may be assigned 0xB. Now the running firmware can selectively choose to accept or ignore commands based on which process is trying to update it.

```cpp
UINT8 token;
```

The component in the device to apply the firmware update.

```cpp
UINT8 componentId;
```

offer interpretation flags:  If we want the in situ firmware to ignore version mismatch (older on top of newer) then set the bit to force Ignore Version.

```cpp
UINT8 forceIgnoreVersion: 1;
```

Forcing immediate reset is asserted with one bit.  If that bit is asserted, the host software expects the in situ firmware cause the device to perform a reset.  The actions of the reset are platform specific.  The device's firmware may choose to take action that swaps banks to make freshly updated firmware the active in situ firmware.  Or not.  It's left up to the implementation of the firmware. The expectation usually is that if the force immediate reset is asserted, that the device will do whatever is necessary to cause the firmware to make the new bank updated become the active firmware running on the target device.

```cpp
UINT8 forceImmediateReset : 1;
```

In the event that the content portion of the offer and content pair involves multiple parts of content.

```cpp
UINT8 segmentNumber;
```

### Processing offers

The ProcessCFWUOffer API accepts two arguments:

```cpp
void ProcessCFWUOffer(FWUPDATE_OFFER_COMMAND* pCommand,
                     FWUPDATE_OFFER_RESPONSE* pResponse)
```

In this use case, assume the user software sends data bytes to the running firmware, then the first message is the offer message.

The offer message is a 16-byte message described above (the FWUPDATE_OFFER_COMMAND structure).

That offer message is the data used by the running firmware to disposition the offer.

During the disposition of the offer, the running firmware notifies the sender by populating fields in the `FWUPDATE_OFFER_RESPONSE` structure.

#### Interpreting the offer

The running firmware should keep track of its state in CFU process. It may be ready/waiting to accept an offer, in the middle of a CFU transaction, or waiting to swap banks between active/inactive firmware.

If the running firmware is in the middle of a CFU transaction - don't accept/process this offer and notify host accordingly.

```cpp
   if (s_currentOffer.updateInProgress)
   {
       memset(pResponse, 0, sizeof (FWUPDATE_OFFER_RESPONSE));

       pResponse->status = FIRMWARE_UPDATE_OFFER_BUSY;
       pResponse->rejectReasonCode = FIRMWARE_UPDATE_OFFER_BUSY;
       pResponse->token = token;
       return;
   }
```

The component ID field of the offer may be used to signal the running firmware that a special action is requested from the running firmware. In the example CFU code, a special offer command is used by the host to retrieve the status of the CFU engine - whether the running software is capable and ready to accept CFU Offers.

```cpp
   else if (componentId == CFU_SPECIAL_OFFER_CMD)
   {
       FWUPDATE_SPECIAL_OFFER_COMMAND* pSpecialCommand =
           (FWUPDATE_SPECIAL_OFFER_COMMAND*)pCommand;
       if (pSpecialCommand->componentInfo.commandCode == CFU_SPECIAL_OFFER_GET_STATUS)
       {
           memset(pResponse, 0, sizeof (FWUPDATE_OFFER_RESPONSE));

           pResponse->status = FIRMWARE_UPDATE_OFFER_COMMAND_READY;
           pResponse->token = token;
           return;
       }
   }
```

Finally, a check is made if there's a bank swap pending.  The bank swap refers to the firmware persisting the information as to whether or not it's still in the process of switching from the running, active application to the newly download image.  

How and where bank switching is performed is an implementation specific task for the embedded firmware.  The CFU protocol and process allows for information to be exchanged between the remote user application conducting the CFU and the in situ firmware that is running.

```cpp
   else if (s_bankSwapPending)
   {
       memset(pResponse, 0, sizeof (FWUPDATE_OFFER_RESPONSE));

       pResponse->status = FIRMWARE_UPDATE_OFFER_REJECT;
       pResponse->rejectReasonCode = FIRMWARE_UPDATE_OFFER_SWAP_PENDING;
       pResponse->token = token;
       return;
   }
```

Finally, if the state of the running firmware isn't busy, and the componentId isn't a special command and there's no bank swap pending - THEN we can process this offer.

Processing an offer involves, but isn't limited to, the four steps outlined below:

##### Step 1 - Check bank

Check the bank of the running application to the bank in the offer.  Are they the same or different?

If the same, then reject the offer (we don't want to overwrite the running/active image).

Else continue.

##### Step 2 - Check hwVariantMask

The running firmware checks the `hwVariantMask` in the offer against the HW it's running on.  This allows the embedded firmware to reject an offer if the offer is invalid for the target. (ex. if the running firmware is on an old HW build and the new offered firmware is meant for a newer, HW build - then the running firmware should reject this offer)

If invalid, then reject the offer.

Else continue.

##### Step 3 - Check firmware version

Check if the version of the firmware content offered has a version older or newer than the current application firmware.

It's left up to the users implementation to decide how to check which firmware is greater than another and if to allow the 'forceIgnoreVersion' field in the offer to be used. Typical firmware development would allow the 'forceIgnoreVersion' field to be used during product development and in debug versions of the firmware but disallowed (not allowing older firmware to be updated on top of new firmware) in product/release firmware.

If this check failed, then reject the offer.

Else continue.

##### Step 4 - Accept offer

The offer is good.  Accept the offer with a response that is tailored for the way messages and status are returned by the firmware to the remote user-application. The so-called "response" is data  (a packed data structure as shown in the demonstration header files) and this data is written out to the user-application by the appropriate means for the device.

### Process the content

The processing of the content is usually a multistep process. The multiple steps refer to the capability of the firmware to accept the firmware image in parts, also known as "blocks" of data.  It isn't always feasible to send the entire image at once to the embedded firmware, so it's realistic to expect the implementation of the CFU protocol and process to accept content in small pieces.

This discussion uses the assumption when describing the process of the CFU content.

The state machine of the content processing involves three states.

1. The state of processing the first block.

1. The state of processing the last block.

1. The state of processing any block in between first and last.

#### The structure of the content command

Like the offer, the content has a structure with fields that are used by the CFU algorithms in the demonstration.

```cpp
typedef struct
{
   UINT8 flags;
   UINT8 length;
   UINT16 sequenceNumber;
   UINT32 address;
   UINT8 pData[MAX_UINT8];
} FWUPDATE_CONTENT_COMMAND;
```

The structure of the content command is simpler than the offer structure. The content is defined as a sequence of bytes to be written into memory.  The preamble of the content is this structure's fields:

1. `UINT8 flags`   Denotes if the content "block" is the first, last or other.

1. `UINT8 length`  Marks the length of the `pData` field.  In the demonstration code for CFU, the limit on the size of the `pData` is 255 bytes.  Other implementations may vary the maximum size of the "block".

1. `UINT16 sequenceNumber`  Marks the index counter of which block is being submitted as content.

1. `UINT32 address`  The address offset of the block.  In the demonstration of CFU of this release, the implementation has predefined information about the physical address of each App region.  For example, a two bank firmware implementation may have App1 begin at address `0x9000` and App2 begin at address `0xA0000`. So, depending on how the firmware image was prepared (S-Records) the address in the SREC may be either the physical address or an offset.  In any case, there needs to be a shared understanding between the preparation of the content and the implementation specific routines of the CFU content processing to determine the true physical address of where to write the block in memory.  It's left up to the firmware developer to adopt best practices and do checks for valid address ranges for each content blog. For example, the CFU code demonstrates a check made if perhaps App1 (meant for `0x9000`) has addresses that overlap into App2, and so on.

1. `UINT8 pData[MAX_UINT8]` - This is the raw bytes of the firmware image block.  Care is taken in the user-application to only put `length` bytes into the complete byte stream of the content block.  

There are no bit fields used in the content structure as per the CFU demonstration from the code provided.

#### The first block

The first block starts the download of the firmware contents.  The firmware running attempts to write the block into non-volatile memory.  Of course the content "block" contains information about where in memory the block should be written, how much data to write and other fields.

Each componentID target device is different and there are multiple methods to persist the data into memory. For example, one componentId could require writing to internal flash, another componentId may write to an external SPI flash or another may utilize another IC's I2C protocol to update its image. The demonstration included with this document highlights the use of a function called `ICompFwUpdateBspWrite` which each unique firmware must implement with knowledge of the underlying non-volatile memory I/O functions of the target it was designed for.

#### Any other block except first or last

The process of accepting new blocks continues when the user-application delivers another block, again with meta data in the message for the address of where the block should be written, how many bytes are contained, and other fields.

The in situ firmware would treat this just like a first block scenario.

However, it should be noted that at any time the system fails to capture and persist the block into memory, it's up to the in situ firmware to respond with a failure code.  

#### The last block

The last block presents a challenge only if the in situ firmware needs to do tasks to validate the image that was just written to the memory.

First, the last block is written to memory.

Then, at a minimum, a CRC check should be made between the data already written to memory (from the first to last blocks) compared to the CRC field in the last block. It's left to each implementation firmware to know how to acquire the CRC for the downloaded image.

Keep in mind that the execution of the CRC check does take time. Unlike the normal flow of the execution of the CFU for offer and block submission.  The last block submission, if it includes a CRC check, will have a certain delay involved just for the fact that the CRC check is potentially examining a large region of memory.  Depending on the target device and other factors this may not be a concern.

> [!IMPORTANT]
> The CRC check of the incoming image is optional and may be commented out. However, best practices should be put into place to at least adopt this check. It is strongly recommended that at this point in the CFU process, other actions are taken to ensure the integrity of the downloaded image. Some of these actions could include verify a 'signed' portion of the image and/or check certificate chains of trust or other best practice approaches to ensuring a secure firmware image. These are left up to the firmware developer.

#### Clean up after last block

Now that the last block is written, and the CRC check is complete, the firmware may respond with a failure if any part of the validation failed.

Otherwise, the expectation is that the CFU process in the firmware will respond with a successful status.

### Forced reset checked

The forced reset flag in the offer is used to determine if the MCU of the target shall undergo a reset (user defined reset).

Typically when a reset is forced, the intent is to cause the MCU to do a reset in order to cause the App bank to switch. Updating persistent variables to denote what firmware image to boot into on reset is left to the firmware developer.
