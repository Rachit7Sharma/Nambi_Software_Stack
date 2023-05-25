/*
 * rosserial Servo Control Example
 *
 * This sketch dmonstrates the control of hobby R/C servos
 * using ROS and the arduiono
 * 
 * For the full tutorial write up, visit
 * www.ros.org/wiki/rosserial_arduino_demos
 *
 * For more information on the Arduino Servo Library
 * Checkout :
 * http://www.arduino.cc/en/Reference/Servo
 */



#include <Servo.h> 
#include <ros.h>
#include <arm/Pwm.h>
#include <std_msgs/UInt16.h>
#include <std_msgs/String.h>
#include <geometry_msgs/Point.h>
#include <sensor_msgs/JointState.h>

ros::NodeHandle  nh;

 int pwm1pin = 12, pwm2pin = 10, dir1,dir2, base_pwm = 8,elbow_pwm = 6,pitch_pwm = 3,roll_pwm = 5;
  int dirpin1=13, dirpin2=11,base_dir = 9,elbow_dir = 7,pitch_dir = 2,roll_dir = 4;
  int xpotpin = A0, ypotpin = A1; 

std_msgs::String str_msg;

//void set_length( const arm::Pwm& cmd_msg)
//{
//  int x = cmd_msg.shoulder_angle;
//  int y = cmd_msg.elbow_angle;
//  //int z = cmd_msg.z;
//
// 
//
////   int xmap = map(x, 0, 90, 285, 940);
////  int ymap = map(y, 0, 60, 60, 980);  
//  int xmap = map(x, 0, 90, 80, 1013);
//  int ymap = map(y, 0, 60, 992, 25);  
//  //int zmap = map(z, 0, 360, 993, 55);
//
//  int xval = analogRead(xpotpin);
//  //Serial.println(xval);
//  int yval = analogRead(ypotpin);
//  //Serial.println(yval);
//  //int zval = analogRead(zpotpin);
//
//  if(xval<xmap)
//  {
//    dir1 = 0;
//    //Serial.println("Increasing");
//  }
//  else if(xval>xmap)
//  {
//    dir1 = 1;
//    //Serial.println("Decreasing");
//  }
//
//  if(yval<ymap)
//  {
//    dir2 = 0;
//  }
//  else if(yval>ymap)
//  {
//    dir2 = 1;
//  }
//
//  /*if(zval>zmap)
//  {
//    dir3 = 1;
//  }
//  else
//  {
//    dir3=0;
//  }*/
//  
//  while((!(xval<(xmap+30) && xval>(xmap-30))) || (!(yval<(ymap+30) && yval>(ymap-30)) ))
//  {
//    xval = analogRead(xpotpin);
//    yval = analogRead(ypotpin);
//    
//    //analogWrite(pwm3pin, 255);
//   
//    //digitalWrite(dirpin3, dir3);
//    
//    if(xval<(xmap+30) && xval>(xmap-30))
//    {
//      analogWrite(pwm1pin, 0);
//    }
//    else
//    {
//      analogWrite(pwm1pin, 255);
//      digitalWrite(dirpin1, dir1);
//      //Serial.println("Here");
//      //Serial.println(yval);
//      
//    }
//
//   if(yval<(ymap+30) && yval>(ymap-30))
//    {
//      analogWrite(pwm2pin, 0);
//    }
//    else
//    {
//      analogWrite(pwm2pin, 255);
//      digitalWrite(dirpin2, dir2);
//      //Serial.println("Here2");
//      //Serial.println(xval);
//      
//    }
//    /*if(zval == zmap)
//    {
//      analogWrite(pwm3pin, 0);
//    }
//    else
//    {
//      analogWrite(pwm1pin, 255);
//      digitalWrite(dirpin1, dir1);
//      
//    }*/
//    char hello6[7] = "InLoop";
//    str_msg.data = hello6;
//    
//  }
//  char hello7[8] = "OutLoop";
//  str_msg.data = hello7;
//  
//  /*int x = map(l, 20, 120, 993, 55);
//  int dir;
//  int val = analogRead(A0);
//  Serial.print("Sensor reading :");
//  Serial.print(val);
//  Serial.println("\n");
//  if(val>x)
//  {
//    dir =1;
//  }
//  else
//  {
//    dir = 0;
//  }
//  while(val!=x)
//  {
//    val=analogRead(A0);
//    analogWrite(pwmpin, 255);
//    digitalWrite(dirpin, dir); 
//  }
//    analogWrite(pwmpin, 0);
//    digitalWrite(dirpin , 0);*/
//}



void servo_cb( const arm::Pwm& cmd_msg){
  digitalWrite(13, HIGH-digitalRead(13));
   
    //toggle led  
  char hello21[12] = "start";
  str_msg.data = "start";

  int val1 = cmd_msg.base;
  if(val1 == 0){
    analogWrite(base_pwm,0);
    char hello[12] = "base val =0";
    str_msg.data = hello;
  }else if(val1>0){
    analogWrite(base_pwm,val1);
    digitalWrite(base_dir,1);
    char hello1[12] = "base val >0";
    str_msg.data = hello1;
  }else{
    val1=-1*val1;
    analogWrite(base_pwm,val1);
    digitalWrite(base_dir,0);
    char hello2[12] = "base val <0";
    str_msg.data = hello2;
  }
  

  int val2 = cmd_msg.gripper;
  if(val2 == 0){
    analogWrite(elbow_pwm,0);
    char hello3[15] = "gripper val =0";
    str_msg.data = hello3;
  }else if(val2>0){
    analogWrite(elbow_pwm,val2);
    digitalWrite(elbow_dir,1);
    char hello4[15] = "gripper val >0";
    str_msg.data = hello4;
  }else{
    val2=-1*val2;
    analogWrite(elbow_pwm,val2);
    digitalWrite(elbow_dir,0);
    char hello5[15] = "gripper val <0";
    str_msg.data = hello5;
  }
  
  int val = cmd_msg.pitch;
  if(val == 0){
    analogWrite(pitch_pwm,0);
    char hello9[13] = "pitch val =0";
    str_msg.data = hello9;
  }else if(val>0){
    analogWrite(pitch_pwm,val);
    digitalWrite(pitch_dir,1);
    char hello10[13] = "pitch val >0";
    str_msg.data = hello10;
  }else{
    val=-1*val;
    analogWrite(pitch_pwm,val);
    digitalWrite(pitch_dir,0);
    char hello11[13] = "pitch val <0";
    str_msg.data = hello11;
  }


  int val4 = cmd_msg.roll;
  if(val4 == 0){
    analogWrite(roll_pwm,0);
    char hello12[12] = "roll val =0";
    str_msg.data = hello12;
  }else if(val4>0){
    analogWrite(roll_pwm,val4);
    digitalWrite(roll_dir,1);
    char hello13[12] = "roll val >0";
    str_msg.data = hello13;
  }else{
    val4=-1*val4;
    analogWrite(roll_pwm,val4);
    digitalWrite(roll_dir,0);
    char hello14[12] = "roll val <0";
    str_msg.data = hello14;
  }

  int val5 = cmd_msg.shoulder_angle;
  if(val5 == 0){
    analogWrite(pwm1pin,0);
    char hello15[16] = "shoulder val =0";
    str_msg.data = hello15;
  }else if(val5>0){
    analogWrite(pwm1pin,val5);
    digitalWrite(dirpin1,0);
    char hello16[16] = "shoulder val >0";
    str_msg.data = hello16;
  }else{
    val5=-1*val5;
    analogWrite(pwm1pin,val5);
    digitalWrite(dirpin1,1                  );
    char hello17[16] = "shoulder val <0";
    str_msg.data = hello17;
  }
  int val6 = cmd_msg.elbow_angle;
  if(val6 == 0){
    analogWrite(pwm2pin,0);
    char hello18[13] = "elbow val =0";
    str_msg.data = hello18;
  }else if(val6>0){
    analogWrite(pwm2pin,val6);
    digitalWrite(dirpin2,1);
    char hello19[13] = "elbow val >0";
    str_msg.data = hello19;
  }else{
    val6=-1*val6;
    analogWrite(pwm2pin,val6);
    digitalWrite(dirpin2,0);
    char hello20[13] = "elbow val <0";
    str_msg.data = hello20;
  }

//  set_length(cmd_msg);  
}

ros::Subscriber<arm::Pwm> sub("set", servo_cb );
ros::Publisher chatter("chatter", &str_msg);

void setup(){
  pinMode(13, OUTPUT);
  pinMode(pwm1pin, OUTPUT);
  pinMode(dirpin1, OUTPUT);
  pinMode(pwm2pin, OUTPUT);
  pinMode(dirpin2, OUTPUT);
  pinMode(base_pwm, OUTPUT);
  pinMode(elbow_pwm, OUTPUT);
  pinMode(pitch_pwm, OUTPUT);
  pinMode(roll_pwm, OUTPUT);
  pinMode(base_dir, OUTPUT);
  pinMode(elbow_dir, OUTPUT);
  pinMode(pitch_dir, OUTPUT);
  pinMode(roll_dir, OUTPUT);
  pinMode(xpotpin, INPUT);
  pinMode(ypotpin, INPUT);
  analogWrite(pwm1pin, 0);
  analogWrite(pwm2pin, 0);
  analogWrite(base_pwm, 0);
  analogWrite(elbow_pwm, 0);
  analogWrite(pitch_pwm, 0);
  analogWrite(roll_pwm, 0);
  nh.initNode();
  
  nh.subscribe(sub);
  nh.advertise(chatter);
}

void loop(){
  chatter.publish( &str_msg );
  nh.spinOnce();
  delay(500);

}
