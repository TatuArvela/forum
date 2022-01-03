class SessionsController < ApplicationController

  def login
    logger.debug "Login"
    @next = true #params[:next]
    @user_is_authenticated = true
  end

  def authenticate
    logger.debug "Authenticate"
    @next = true #params[:next]
    @user_is_authenticated = true

    user = User.find_by(username: params[:username].downcase)
    if false #user && user.authenticate(params[:password])
      log_in user
      redirect to @next
    else
      @form_errors = true
      render 'login'
    end
  end

  def logout
    render 'logged_out'
  end
end
