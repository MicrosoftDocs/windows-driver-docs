---
title: Threading Models
description: Threading Models
ms.assetid: 3BB0C01B-D82B-45dd-8AC8-EA2E2811CD24
---

# Threading Models


TAEF provides functionality for pre-configuring a COM threading model for the environment where you test execute. By default, Managed ©\#) and Script tests run on STA thread; for Native, threading model is not pre-configured.

The "ThreadingModel" metadata property is used to request a threading model. The supported values for this property are:

| Property Value | Description                                                                               |
|----------------|-------------------------------------------------------------------------------------------|
| STA            | Single-Threaded Apartment (CoInitializeEx is called with COINIT\_APARTMENTTHREADED flag). |
| MTA            | Multithreaded Apartment (CoInitializeEx is called with COINIT\_MULTITHREADED flag).       |
| None           | Threading model is not specified.                                                         |

 

## <span id="Configuring_a_threading_model"></span><span id="configuring_a_threading_model"></span><span id="CONFIGURING_A_THREADING_MODEL"></span>Configuring a threading model


Example: To request MTA threading model from C++ mark-up:

```
class ThreadModelTests
{

    TEST_CLASS(ThreadModelTests);

    BEGIN_TEST_METHOD(MTAThreadingModelTest)
        TEST_METHOD_PROPERTY(L"ThreadingModel", L"STA")
    END_TEST_METHOD()
};
```

You can also request threading model property for a class or a module. For example,

```
class ThreadModelTestsWithMTADefault
{

    BEGIN_TEST_CLASS(ThreadModelTestsWithMTADefault)
        TEST_CLASS_PROPERTY(L"ThreadingModel", L"Mta")
    END_TEST_CLASS()

    TEST_METHOD(DefaultWithMTASetByClass);
};
```

Similarly, you can also request threading model for managed tests:

```
[TestClass]

public class SimpleTests
{
    [TestMethod]
    [TestProperty("ThreadingModel", "MTA")]
    public void Test1()
    {
        Verify.IsTrue(true);
    }

    [TestMethod]
    [TestProperty("ThreadingModel", "STA")]
    public void Test2()
    {
        Verify.IsTrue(true);
    }

    [TestMethod]
    [TestProperty("ThreadingModel", "{STA; MTA}")]
    public void SetsOfMetadataTest()
    {
        Log.Comment("In CSharpThreadingModelExample.SetsOfMetadataTest");
        DisplayAppartmentState();
    }
}
```

Notice in the last test above: SetsOfMetadataTest, it is also possible to make use of metadata sets and run the same test: first with STA threading model and then with MTA.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[taef\taef]:%20Threading%20Models%20%20RELEASE:%20%289/12/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




