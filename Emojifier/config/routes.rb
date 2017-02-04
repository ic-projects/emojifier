Rails.application.routes.draw do

  resources :items
  root 'welcome#index'

  get 'welcome/pyscript'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
