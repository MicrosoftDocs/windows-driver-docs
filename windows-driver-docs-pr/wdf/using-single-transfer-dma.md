# Using Single Transfer DMA

By default, WDF frequently splits a single DMA transaction into multiple DMA transfers. However, some devices cannot handle a fragmented transaction and must instead receive all data in a single DMA operation.  For example, some PCI network controllers require one network packet at a time because they do not have the hardware to cache and reassemble partial data.

Starting with KMDF version 1.19, a KMDF driver using DMA v3 can request that WDF send each individual DMA transaction as a single transfer.  There are two ways that a driver can request single transfer DMA: 

* The driver can call WdfDmaTransactionSetSingleTransferRequirement.
* To set the single-transfer requirement for all DMA transactions created with a particular DMA enabler, specify the WDF_DMA_ENABLER_CONFIG_REQUIRE_SINGLE_TRANSFER flag when calling WdfDmaEnablerCreate. This is equivalent to calling WdfDmaTransactionSetSingleTransferRequirement for each transaction object created with the enabler. Using this flag instead of calling WdfDmaTransactionSetSingleTransferRequirement also makes this setting persist when the transaction object is [recycled](https://msdn.microsoft.com/en-us/library/windows/hardware/ff547114) and reinitialized. Otherwise, it would be reset similarly to other transaction-level properties, like immediate execution and maximum transfer length. (links? md comments. code themes. shortcut for link)


1. Call WdfDmaTransactionCreate.
2. Call WdfDmaTransactionSetSingleTransferRequirement.
3. Call WdfDmaTransactionInitialize.  If initialization fails due to transaction fragmentation, a driver has the option of failing the I/O request or rearranging the transaction�s memory buffers in a supported manner, and reinitializing the transaction.
4. Call WdfDmaTransactionExecute.  The transaction should complete in a single DMA transfer.

(copy red from xml)
(add new versions in histories, add new for 1.19, including wdf too many transfers error code)

link to old DMA pcage with classic diagram

This flag is intended for drivers that want all DMA transactions to be single-transfer, so they don�t have to call WdfDmaTransactionSetSingleTransferRequirement each time they create or reuse a transaction object. Since transactions inherit this value from the enabler, it also means that it persists when a transaction is reused.


This is consistent with other per-transaction properties a driver may set, like immediate execution and overriding the transaction�s maximum transfer length. (link?)


The requirements are:
1.	Transaction's total length is at most the device's maximum transfer size. If this check fails, return STATUS_WDF_TOO_MANY_TRANSFERS.
2.	The number of map registers needed to map the transaction is not larger than the number the DMA adapter has reserved. If this check fails, return STATUS_WDF_TOO_MANY_TRANSFERS.
3.	The length of the Scatter/Gather list that describes the mapped transfer is within the device's supported limit (max 1 for Packet profile DMA). If this check fails, return STATUS_WDF_TOO_FRAGMENTED.
a.	Returning STATUS_WDF_TOO_FRAGMENTED here instead of STATUS_WDF_TOO_MANY_TRANSFERS is consistent with other paths where we fail the DMA request because the SG element limit is exceeded.
4.	The preallocated SG list buffer is large enough to hold the SG list needed to describe the transfer. If it is not, then we can allocate a large enough buffer from non-paged system memory to replace it. If the new buffer allocation fails, return STATUS_INSUFFICIENT_RESOURCES.
a.	The SG buffer reallocation happens in the initialize path in order to reduce the risk of failure during transaction execution.


STATUS_WDF_TOO_MANY_TRANSFERS may be returned by WdfDmaTransactionInitialize if a DMA transaction marked with m_RequireSingleTransfer==TRUE cannot be completed with a single DMA operation.
It is also returned by WdfDmaTransactionDmaCompletedWithLength and WdfDmaTransactionDmaCompletedFinal if the device reports a transferred length less than m_TransactionLength (residual transfer).
This new error code is declared in wdfstatus.mc, along with all other WDF-specific NTSTATUS values. We do not reuse the existing STATUS_WDF_TOO_FRAGMENTED because it describes a specific failure in scatter/gather DMA: when the number of map registers required to map a transfer exceed the maximum supported number of scatter/gather elements as declared by the driver.

