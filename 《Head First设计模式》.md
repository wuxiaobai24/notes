# 设计模式

## 策略模式

> 策略模式定义了算法族，分别封装起来，让他们之间可以相互替换，策略模式让算法的实现独立与使用算法的客户

- 设计原则
  - 找出应用中变化的地方，把他们独立出来
  - 针对接口编程，而不是针对实现编程
  - 多用组合(HAS-A),少用继承(IS_A)

> 策略模式的大概思路是把对象中一些可能会改变的行为抽出来做个接口，对这个接口的不同实现构成了算法族，在原来的类中加入一个这个接口的实例变量和对应的setter就可以动态的改变行为的实现。

在编写OO程序的时候，我们经常会遇到，类的某个行为经常要改变，甚至是需要动态的改变，这时我们就可以使用 **策略模式** 了。

比如说，Duck类中的Fly方法和Quack方法，不同的Duck的Fly和Quack方法可能会不一样，如果直接把常用的Fly方法和Quack方法直接写在Duck类中，有需要时再覆盖的话，一旦需求出现改变，那么要在每一个类中进行修改大量的使用Ctrl-C和Ctrl-V，这显然不是我们想要的。

使用策略模式的话，我们可以把Fly方法和Quack方法抽出来做成FlyBehavior和QuackBehavior接口，通过实现这个接口的不同类形成这个行为的算法族，在Duck类中我们设置FlyBehavior和QuackBehavior的实例变量，通过接受不同的FlyBehavior和QuackBehavior实现类的的实例来实现不同行为的变换。

实例：

Duck类
```Java
public abstract class Duck {
    FlyBehavior flyBehavior;
    QuackBehavior quackBehavior;

    public Duck(){
    }

    public abstract void display(); //这个是需要子类实现的

    public void performFly(){
        flyBehavior.fly();
    }

    public void performQuack(){
        quackBehavior.quack();
    }

    public void swin(){
        System.out.println("All ducks float, even decoys.");
    }

    public void setFlyBehavior(FlyBehavior fb){
        flyBehavior = fb;
    }

    public void setQuackBehavior(QuackBehavior qb){
        quackBehavior = qb;
    }
}
```
FlyBehavior接口
```Java
public interface FlyBehavior {
    public void fly();
}
```
QuackBehavior接口
```Java
public interface QuackBehavior {
    public void quack();
}
```
QuackBehavior借口的实现
```Java
public class Quack implements QuackBehavior {
    public void quack(){
        System.out.println("quack");
    }
}
```
```Java
public class MuteQuack implements QuackBehavior {
    public void quack(){
        System.out.println("<< Silence >>");
    }
}
```
```Java
public class Squeak implements QuackBehavior {
    public void quack(){
        System.out.println("Squeak");
    }
}
```

FlyBehavior接口的实现
```Java
public class FlyWithWings implements FlyBehavior {
    public void fly(){
        System.out.println("I'm flying!!");
    }
}
```
```Java
public class FlyNoWay implements FlyBehavior {
    public void fly(){
        System.out.println("I can't fly.");
    }
}
```
MallardDuck类
```Java
public class MallardDuck extends Duck {
    public MallardDuck(){
        quackBehavior = new Squeak();
        flyBehavior = new FlyWithWings();
    }

    @Override
    public void display() {
        System.out.println("I'm a real Mallard Duck.");
    }
}
```
测试
```Java
public class MiniDuckSimulator {
    public static void main(String[] args){
        Duck mallard = new MallardDuck();
        mallard.performFly();
        mallard.performQuack();
        mallard.setFlyBehavior(new FlyNoWay());
        mallard.performFly();
        //Java8的话可以写的更优雅一些
        mallard.setQuackBehavior(() ->{
            System.out.println("Queak");
        });
        mallard.performQuack();
    }
}
```
