/// <reference types="Cypress" />
beforeEach(function(){
    cy.visit("https://taaghche.com/")


})
describe('open goodreads', function (){2
    const paswword = 'ئخشن564865'
    it('Attributes - login ', function (){
        cy.get('.profileDropdown_login__1mKoW').click()
        cy.get('.textField_container__3FYko > input').click().type('09333974776')
        cy.get('[data-cy="loading-button"]').click()
        cy.wait(10)
        cy.get('.loginModal_closeIcon__1aHJI').click()
        cy.get('.passwordField_container__uH8aU > input').click().type(paswword)
        cy.get(':nth-child(2) > [data-cy="loading-button"]').click()
        cy.get('.filter_title__3Rmpw').should("have.class", "filter_title__3Rmpw")
        cy.get('header.header_container__hVzZT div').eq(12)
        .should('have.length', 1)
        .first()
        .should('have.text', 'Walk the dog')

    })


     it("Attributes- search book and add book ", function(){
        const newItem = 'نجات از هزار تو'
        const   email = 'mohsen.ak136504@gmail.com'
        cy.get('.autocomplete_searchInput__1cYwH').type(newItem)
        cy.get('.autocomplete_search__234Gp').click()
        cy.wait(20)
        cy.get('.searchBookList_bookList__3d-mV > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > img:nth-child(2)').click()
        //cy.get('.loginModal_closeIcon__1aHJI').click()
        cy.get('.price_label__gGB0i').click()
        
        cy.get('div[id="__next"] div').eq(3).click()
        cy.get('div#content-title').should("have.id", "content-title")
        cy.get('div.title').should('have.length', 1);


        

     })


    
    
})