---
title: Programming Considerations
description: Programming Considerations
ms.assetid: 5f51352a-cfbb-4fa0-98af-953b151a4563
keywords:
- Network Module Registrar WDK , programming considerations
- NMR WDK , programming considerations
- reference counts WDK Network Module Registrar
- in-progress calls WDK Network Module Registrar
- counting references WDK Network Module Registrar
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Programming Considerations


A network module should use some form of reference counting to keep track of the number of in-progress calls to an attached network module's [Network Programming Interface (NPI)](network-programming-interface.md) functions. This will facilitate detaching from an attached network module when one of the two network modules deregisters with the NMR. A network module cannot complete detachment until there are no in-progress calls to the attached network module's NPI functions. A network module must also ensure that no more calls to the previously attached network module will be initiated once the network modules are detached.

For example, a client module might use an implementation similar to the following for tracking the number of in-progress calls to an attached provider module's NPI functions:

```C++
// Context structure for the client&#39;s binding to a provider module
typedef struct CLIENT_BINDING_CONTEXT_ {
  LIST_ENTRY Link;
  HANDLE NmrBindingHandle;
  PVOID ProviderBindingContext;
  PEXNPI_PROVIDER_DISPATCH ProviderDispatch;
  KSPIN_LOCK DetachLock;
  LONG InProgressCallCount;
  LONG Detaching;
  .
  . // Other client-specific members
  .
} CLIENT_BINDING_CONTEXT, *PCLIENT_BINDING_CONTEXT;

// Pool tag used for allocating the binding context
#define BINDING_CONTEXT_POOL_TAG &#39;tpcb&#39;

// Structure for the client&#39;s dispatch table
const EXNPI_CLIENT_DISPATCH Dispatch = {
  .
  . // Function pointers to the client module&#39;s
  . // NPI callback functions
  .
};

// Head of linked list of binding context structures
LIST_ENTRY BindingContextList;

// Spin lock for binding context list
KSPIN_LOCK BindingContextListLock;

// Prototype for the client module&#39;s unload function
VOID
  Unload(
    PDRIVER_OBJECT DriverObject
    );

// Variable to contain the handle for the registration
HANDLE ClientHandle;

// DriverEntry function
NTSTATUS
  DriverEntry(
    PDRIVER_OBJECT DriverObject,
    PUNICODE_STRING RegistryPath
    )
{
  NTSTATUS Status;

  // Specify the unload function
  DriverObject->DriverUnload = Unload;

  // Initialize the binding context list spin lock
  KeInitializeSpinLock(
    &BindingContextListLock
    );

  // Initialize the binding context list head
  InitializeListHead(
    &BindingContextList
    );

  .
  . // Other initialization tasks
  .

  // Register the client module with the NMR
  Status = NmrRegisterClient(
    &ClientCharacteristics,
    &ClientRegistrationContext,
    &ClientHandle,
    );

  // Return the result of the registration
  return Status;
}

// ClientAttachProvider callback function
NTSTATUS
  ClientAttachProvider(
    IN HANDLE NmrBindingHandle,
    IN PVOID ClientContext,
    IN PNPI_REGISTRATION_INSTANCE ProviderRegistrationInstance
    )
{
  PNPI_MODULEID ProviderModuleId;
  PEXNPI_PROVIDER_CHARACTERISTICS ProviderNpiSpecificCharacteristics;
  PCLIENT_BINDING_CONTEXT BindingContext;
  PVOID ProviderBindingContext;
  PEXNPI_PROVIDER_DISPATCH ProviderDispatch;
  KLOCK_QUEUE_HANDLE BindingContextListLockHandle;
  NTSTATUS Status;

  // Get pointers to the provider module&#39;s identification structure
  // and the provider module&#39;s NPI-specific characteristics structure
  ProviderModuleId = ProviderRegistrationInstance->ModuleId;
  ProviderNpiSpecificCharacteristics =
    (PEXNPI_PROVIDER_CHARACTERISTICS)
      ProviderRegistrationInstance->NpiSpecificCharacteristics;

  //
  // Use the data in the structures pointed to by
  // ProviderRegistrationInstance, ProviderModuleId,
  // and ProviderNpiSpecificCharacteristics to determine
  // whether to attach to the provider module.
  //

  // If the client module determines that it will not attach
  // to the provider module
  if (...)
  {
    // Return status code indicating the modules did not
    // attach to each other
    return STATUS_NOINTERFACE;
  }

  // Allocate memory for the client&#39;s binding context structure
  BindingContext =
    (PCLIENT_BINDING_CONTEXT)
      ExAllocatePoolWithTag(
        NonPagedPool,
        sizeof(CLIENT_BINDING_CONTEXT),
        BINDING_CONTEXT_POOL_TAG
        );

  // Check result of allocation
  if (BindingContext == NULL)
  {
    // Return error status code
    return STATUS_INSUFFICIENT_RESOURCES;
  }

  // Initialize the client binding context structure
  KeInitializeSpinLock(
    &BindingContext->DetachLock
   );
  BindingContext->InProgressCallCount = 0;
  BindingContext->Detaching = 0;
  ...

  // Continue with the attachment to the provider module
  Status = NmrClientAttachProvider(
    NmrBindingHandle,
    BindingContext,
    &Dispatch,
    &ProviderBindingContext,
    &ProviderDispatch
    );

  // Check result of attachment
  if (Status == STATUS_SUCCESS)
  {
    // Save NmrBindingHandle, ProviderBindingContext,
    // and ProviderDispatch for future reference
    BindingContext->NmrBindingHandle =
      NmrBindingHandle;
    BindingContext->ProviderBindingContext =
      ProviderBindingContext;
    BindingContext->ProviderDispatch =
      ProviderDispatch;

    // Acquire the binding context list spin lock
    KeAcquireInStackQueuedSpinLock(
      &BindingContextListLock,
      &BindingContextListLockHandle
      );

    // Add this binding context to the list of valid
    // binding contexts
    InsertTailList(
      &BindingContextList,
      &BindingContext->Link
      );
 
    // Release the binding context list spin lock
    KeReleaseInStackQueuedSpinLock(
      &BindingContextListLockHandle
      );
  }

  // Attachment did not succeed
  else
  {
    // Free memory for client&#39;s binding context structure
    ExFreePoolWithTag(
      BindingContext,
      BINDING_CONTEXT_POOL_TAG
      );
  }

  // Return result of attachment
  return Status;
}

// Wrapper function around a provider NPI function
//
// Each of the provider NPI functions should be wrapped
// in this manner.
NTSTATUS
  ProviderNpiFunctionXxx(
    ClientBindingContext,
    .
    . // Parameters to the provider NPI function
    .
    )
{
  KLOCK_QUEUE_HANDLE BindingContextListLockHandle;
  KLOCK_QUEUE_HANDLE DetachLockHandle;
  PCLIENT_BINDING_CONTEXT BindingContextListElement;
  PLIST_ENTRY Entry;
  NTSTATUS Status;

  // Acquire the binding context list spin lock
  KeAcquireInStackQueuedSpinLock(
    &BindingContextListLock,
    &BindingContextListLockHandle
    );

  // Search for the binding context in the list of valid
  // binding contexts
  for (Entry = BindingContextList.Flink;
       Entry != &BindingContextList;
       Entry = Entry->Flink)
  {
    // Get the next binding context from the list
    BindingContextListElement =
      CONTAINING_RECORD(
        Entry,
        CLIENT_BINDING_CONTEXT,
        Link
        );

    // Check if this binding context is a match
    if (BindingContextListElement == ClientBindingContext)
    {
      // Break out of the search loop
      break;
    }
  }

  // Check if the binding context was not found
  if (Entry == &BindingContextList)
  {
    // Release the binding context list spin lock
    KeReleaseInStackQueuedSpinLock(
      &BindingContextListLockHandle
      );

    // Return status indicating that the interface is not available
    return STATUS_NOINTERFACE;
  }

  // Acquire the detach spin lock at DPC level
  KeAcquireInStackQueuedSpinLockAtDpcLevel(
    &ClientBindingContext->DetachLock,
    &DetachLockHandle
    );

  // The modules should not be detaching
  ASSERT(ClientBindingContext->Detaching != 1);

  // Increment the in-progress call count
  ClientBindingContext->InProgressCallCount++;

  // Release the detach spin lock from DPC level
  KeReleaseInStackQueuedSpinLockFromDpcLevel(
    &DetachLockHandle
    );

  // Release the binding context list spin lock
  KeReleaseInStackQueuedSpinLock(
    &BindingContextListLockHandle
    );

  // Call the provider NPI function
  Status =
    ClientBindingContext->ProviderDispatch->ProviderNpiFunctionXxx(
      ClientBindingContext->ProviderBindingContext,
      .
      . // Parameters to the provider NPI function
      .
      );

  // Check if pending
  if (Status == STATUS_PENDING)
  {
    // If completion of the call is pending, then when the call
    // completes, the completion routine (or other callback function
    // that is called upon completion of the call) must include the
    // the same code as below for the non-pending case.

    // Return pending status
    return STATUS_PENDING;
  }

  // Acquire the detach spin lock
  KeAcquireInStackQueuedSpinLock(
    &ClientBindingContext->DetachLock,
    &DetachLockHandle
    );

  // Decrement the in-progress call count
  ClientBindingContext->InProgressCallCount--;

  // Check if the modules are now detaching
  if (ClientBindingContext->Detaching == 1)
  {
    // Check if this call was the last of the in-progress
    // calls to the provider module to be completed
    if (ClientBindingContext->InProgressCallCount == 0)
    {
      // Release the detach spin lock
      KeReleaseInStackQueuedSpinLock(
        &DetachLockHandle
        );

      // Inform the NMR that detachment is complete
      NmrClientDetachProviderComplete(
        ClientBindingContext->NmrBindingHandle
        );
    }
    else
    {
      // Release the detach spin lock
      KeReleaseInStackQueuedSpinLock(
        &DetachLockHandle
        );
    }
  }
  else
  {
    // Release the detach spin lock
    KeReleaseInStackQueuedSpinLock(
      &DetachLockHandle
      );
  }

  // Return status of the call to the provider NPI function
  return Status;
}

// ClientDetachProvider callback function
NTSTATUS
  ClientDetachProvider(
    IN PVOID ClientBindingContext
    )
{
  PCLIENT_BINDING_CONTEXT BindingContext;
  KLOCK_QUEUE_HANDLE BindingContextListLockHandle;
  KLOCK_QUEUE_HANDLE DetachLockHandle;
  NTSTATUS Status;

  // Get a pointer to the binding context
  BindingContext = (PCLIENT_BINDING_CONTEXT)ClientBindingContext;

  // Acquire the binding context list spin lock
  KeAcquireInStackQueuedSpinLock(
    &BindingContextListLock,
    &BindingContextListLockHandle
    );

  // Remove the binding context from the binding context list
  RemoveEntryList(&BindingContext->Link);

  // Acquire the detach spin lock at DPC level
  KeAcquireInStackQueuedSpinLockAtDpcLevel(
    &BindingContext->DetachLock,
    &DetachLockHandle
    );

  // Set the flag indicating that the client module is detaching
  // from the provider module so that the completion of the final
  // call will complete the detachment
  BindingContext->Detaching = 1;

  // Check if there are no in-progress NPI function calls to the
  // provider module
  if (BindingContext->InProgressCallCount == 0)
  {
    // Set the status to success to indicate detachment is complete
    Status = STATUS_SUCCESS;
  }

  // There are one or more in-progress NPI function calls
  // to the provider module
  else
  {
    // Set the status to pending to indicate that detachment is
    // pending completion of the in-progress NPI function calls
    Status = STATUS_PENDING;
  }

  // Release the detach spin lock from DPC level
  KeReleaseInStackQueuedSpinLockFromDpcLevel(
    &DetachLockHandle
    );

  // Release the binding context list spin lock
  KeReleaseInStackQueuedSpinLock(
    &BindingContextListLockHandle
    );

  // Return the status of the detachment
  return Status;
}
```

Likewise, a provider module might use an implementation along the same lines as the above client module example for tracking the number of in-progress calls to an attached client module's NPI callback functions.

**Note**  The above code example shows one possible method of tracking the number of in-progress calls to an attached network module's NPI functions. A network module might use an alternate method depending on the implementation details of the particular NPI that the network module supports.

 

 

 





