import { Component, OnInit, Input } from '@angular/core';

import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-wines',
  templateUrl: './wines.component.html',
  styleUrls: ['./wines.component.css']
})
export class WinesComponent implements OnInit {

  constructor(private service:SharedService) { }

  cartId:any=[];
  wineList:any=[];

  ngOnInit(): void {
    this.getWinesList();
    this.getCartId();
  }

  getWinesList(){
    this.service.getWines().subscribe(data => {
      this.wineList=data;
    });
  }

  getCartId(){
    this.service.getCart().subscribe(data => {
      this.cartId=data;
    });
  }

}
