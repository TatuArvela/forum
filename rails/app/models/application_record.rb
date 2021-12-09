class ApplicationRecord < ActiveRecord::Base
  self.abstract_class = true

  before_create :update_created_by
  before_update :update_updated_by

  def update_created_by
    self.created_by_id = current_user.id if defined?(current_user)
  end

  def update_updated_by
    self.updated_by_id = current_user.id if defined?(current_user)
  end
end
