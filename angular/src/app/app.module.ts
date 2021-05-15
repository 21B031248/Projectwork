import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { WinesComponent } from './compoments/wines/wines.component';
import { NavbarComponent } from './compoments/navbar/navbar.component';
import { CartComponent } from './compoments/cart/cart.component';
import { CheckoutComponent } from './compoments/checkout/checkout.component';
import { AddEditComponent } from './compoments/cart/add-edit/add-edit.component';
import { CartItemComponent } from './compoments/cart/cart-item/cart-item.component';

import { SharedService } from './shared.service';

import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    WinesComponent,
    NavbarComponent,
    CartComponent,
    CheckoutComponent,
    AddEditComponent,
    CartItemComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [
    SharedService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
