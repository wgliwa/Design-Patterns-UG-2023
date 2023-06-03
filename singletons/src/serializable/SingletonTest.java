package serializable;

import org.junit.Test;

import static org.junit.Assert.*;

import java.io.*;

public class SingletonTest {

    @Test
    public void defaultSingletonTest() throws IOException, ClassNotFoundException {
        Singleton instance1 = Singleton.getInstance();
        ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("singleton.ser"));
        out.writeObject(instance1);
        out.close();

        ObjectInputStream in = new ObjectInputStream(new FileInputStream("singleton.ser"));
        Singleton instance2 = (Singleton) in.readObject();
        in.close();

        System.out.println("no match " + instance1.hashCode() + " " + instance2.hashCode());
        assertNotEquals(instance1, instance2);
    }

    @Test
    public void singletonSerTest() throws IOException, ClassNotFoundException {
        SingletonSer instance1 = SingletonSer.getInstance();
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("singleton.ser"));
        oos.writeObject(instance1);
        oos.close();

        ObjectInputStream ois = new ObjectInputStream(new FileInputStream("singleton.ser"));
        SingletonSer instance2 = (SingletonSer) ois.readObject();
        ois.close();

        System.out.println("match " + instance1.hashCode() + " " + instance2.hashCode());
        assertEquals(instance1, instance2);
    }
}