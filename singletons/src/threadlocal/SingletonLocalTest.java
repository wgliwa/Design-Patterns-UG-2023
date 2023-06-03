package threadlocal;
import org.junit.Test;

import java.io.IOException;


public class SingletonLocalTest {
    @Test
    public void defaultSingletonTest()throws IOException, ClassNotFoundException {
        Thread t1 = new Thread(()->System.out.println(Singleton.getInstance().hashCode()));
        Thread t2 = new Thread(()->System.out.println(Singleton.getInstance().hashCode()));
        t1.start();
        t2.start();
    }
    @Test
    public void localSingletonTest()throws IOException, ClassNotFoundException {
        Thread t1 = new Thread(()->System.out.println(LocalSingleton.getInstance().hashCode()));
        Thread t2 = new Thread(()->System.out.println(LocalSingleton.getInstance().hashCode()));
        t1.start();
        t2.start();
    }

}