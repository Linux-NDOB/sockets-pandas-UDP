import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CalendarModel } from 'src/app/Models/Calendar.models';
import { CalendarService } from 'src/app/Services/Calendar.services';
import { DataService } from 'src/app/Services/Data.service';
import Swal from 'sweetalert2';

import {
  IMqttMessage,
  IMqttServiceOptions,
  MqttService,
  IPublishOptions,
} from 'ngx-mqtt';
import { IClientSubscribeOptions } from 'mqtt-browser';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-listado-timbres-page',
  templateUrl: './listado-timbres-page.component.html',
  styleUrls: ['./listado-timbres-page.component.css']
})
export class ListadoTimbresPageComponent implements OnInit {

  public Calendar: CalendarModel[];

  constructor(private _CalendarService: CalendarService, private _DataService: DataService, private _Router: Router, private _mqttService: MqttService) {
    this.Calendar = this._CalendarService.Calendar;
    this.client = this._mqttService;

  }

  ngOnInit(): void {
    this.createConnection();
  }


  Eliminar(Id: number, Pos: number) {
    Swal.fire({
      title: 'Eliminar registro',
      text: "Desea eliminar este Registro?",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Confirmar',
      cancelButtonText: 'Cancelar'
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire(
          'Registro eliminado exitosamente',
          '********************',
          'success'

        )
        this._CalendarService.DeleteCalendar(Pos)
        this._DataService.deleteCalendar(Id).subscribe(
          e => console.log(e)
        )
      }
    })
  }

  Editar(id: number) {
    Swal.fire({
      title: 'Actualizar Registro',
      text: "Desea Actualizar este Registro?",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Confirmar',
      cancelButtonText: 'Cancelar'
    }).then((result) => {
      if (result.isConfirmed) {
        this._Router.navigate(["TimbreAutomatico?/Home/Registros/UpdateReg/", id])

      }
    })
  }

  private curSubscription: Subscription | undefined;
  connection = {
    hostname: '192.168.100.231',
    port: 9001,
    //path: '/mqtt',
    //clean: true, // Retain session
    //connectTimeout: 4000, // Timeout period
    //reconnectPeriod: 4000, // Reconnect period
    // Authentication information
    clientId: 'mqttx_597046f4',
    username: 'emqx_test',
    password: 'emqx_test',
    protocol: 'ws',
  }
  subscription = {
    topic: 'cmnd/rasmota/Power',
    qos: 0,
  };
  publish = {
    topic: 'cmnd/tasmota/Power',
    qos: 0,
    payload: 'ON',
  };
  off = {
    topic: 'cmnd/tasmota/Power',
    qos: 0,
    payload: 'OFF',
  };
  receiveNews = '';
  qosList = [
    { label: 0, value: 0 },
    { label: 1, value: 1 },
    { label: 2, value: 2 },
  ];
  client: MqttService | undefined;
  isConnection = false;
  subscribeSuccess = false;

  // Create a connection
  createConnection() {
    // Connection string, which allows the protocol to specify the connection method to be used
    // ws Unencrypted WebSocket connection
    // wss Encrypted WebSocket connection
    // mqtt Unencrypted TCP connection
    // mqtts Encrypted TCP connection
    try {
      this.client?.connect(this.connection as IMqttServiceOptions)
    } catch (error) {
      console.log('mqtt.connect error', error);
    }
    this.client?.onConnect.subscribe(() => {
      this.isConnection = true
      console.log('Connection succeeded!');
    });
    this.client?.onError.subscribe((error: any) => {
      this.isConnection = false
      console.log('Connection failed', error);
    });
    this.client?.onMessage.subscribe((packet: any) => {
      this.receiveNews = this.receiveNews.concat(packet.payload.toString())
      console.log(`Received message ${packet.payload.toString()} from topic ${packet.topic}`)
    })
  }

  // 订阅主题
  doSubscribe() {
    const { topic, qos } = this.subscription
    this.curSubscription = this.client?.observe(topic, { qos } as IClientSubscribeOptions).subscribe((message: IMqttMessage) => {
      this.subscribeSuccess = true
      console.log('Subscribe to topics res', message.payload.toString())
    })
  }
  // 取消订阅
 
  // 发送消息
  doPublish() {
    const { topic, qos, payload } = this.publish
    console.log(this.publish)
    this.client?.unsafePublish(topic, payload, { qos } as IPublishOptions)
  }

  doOff() {
    const { topic, qos, payload } = this.off
    console.log(this.publish)
    this.client?.unsafePublish(topic, payload, { qos } as IPublishOptions)
  }
}

