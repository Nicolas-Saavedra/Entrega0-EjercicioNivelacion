{
  description = "A flake to setup a Nodejs env";

  inputs = {
    nixpkgs.url = "nixpkgs/nixos-unstable";
  };

  outputs =
    { self, nixpkgs }:
    {
      devShells.x86_64-linux.default =
        let
          pkgs = import nixpkgs { system = "x86_64-linux"; };
        in
        pkgs.mkShell {
          buildInputs = with pkgs; [
            nodejs_22
            yarn
          ];

          # Optional: Define any shell hooks or additional environment variables
          shellHook = ''
            yarn
          '';
        };
    };
}
